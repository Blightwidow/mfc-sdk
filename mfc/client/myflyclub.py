import os

import requests
from requests_ratelimiter import LimiterAdapter  # type: ignore

from mfc.client.cache import MyFlyClubCache

AUTH_COOKIE = "cf_clearance"


class _MyFlyClubClient:
    def __init__(self):
        self.base_url = "https://myfly.club"
        self.session = requests.Session()
        self.session.headers.update(
            {
                "Accept": "application/json, text/plain, */*",
                "Accept-Encoding": "gzip, deflate, br",
                "Accept-Language": "en-US,en;q=0.9",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
            }
        )
        # Apply a rate-limit (5 requests per second) to all requests
        adapter = LimiterAdapter(
            per_second=1000 / int(os.environ.get("MYFLY_REQUESTS_INTERVAL", 200)),
            max_retries=3,
        )
        self.session.mount("http://", adapter)
        self.session.mount("https://", adapter)
        self.id: int | None = None
        self.cache = MyFlyClubCache()

    def login(self) -> str:
        """Login method to authenticate the user.
        Returns:
            str: The cf_clearance cookie value.
        Raises:
            requests.exceptions.HTTPError: If the login request fails.
            ValueError: If the login fails and no cookie is found in the response.
        """
        username = os.getenv("MYFLY_USERNAME")
        password = os.getenv("MYFLY_PASSWORD")

        if username is None or password is None:
            raise ValueError(
                "Username and password must be provided as environment variables. See .env.example for more details."
            )

        response = self.session.post(
            f"{self.base_url}/login", auth=(username, password)
        )
        response.raise_for_status()
        cookie = response.cookies.get("PLAY_SESSION")

        if cookie is None:
            raise ValueError("Login failed. No cookie found in the response.")

        self.session.cookies.update(
            {
                AUTH_COOKIE: cookie,
            }
        )
        self.id = response.json().get("id")

        return cookie

    def request(self, method: str, path: str, payload: dict | None = None) -> dict:
        """Getter method to retrieve data from the API.
        Args:
            path (str): The API endpoint to retrieve data from, with a leading slash.
        Returns:
            dict: The JSON response from the API.
        Raises:
            requests.exceptions.HTTPError: If the request to the API fails.
            ValueError: If the path does not start with a leading slash or if the session cookie is not found.
        """
        if not path.startswith("/"):
            raise ValueError("Path must start with a leading slash.")

        if not self.id:
            self.login()

        response = self.session.get(f"{self.base_url}/current-cycle")
        response.raise_for_status()

        cycle = response.json().get("cycle")
        cached_answer = self.cache.get(cycle, path)
        if cached_answer is not None:
            return cached_answer

        response = self.session.request(
            method=method, url=f"{self.base_url}{path}", json=payload
        )
        response.raise_for_status()
        data = response.json()
        self.cache.set(cycle, path, data)
        return data

    def get(self, path: str) -> dict:
        return self.request("GET", path)

    def post(self, path: str, payload: dict) -> dict:
        return self.request("POST", path, payload)


mfc_client = _MyFlyClubClient()
