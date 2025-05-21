class MyFlyClubCache:
    """
    A simple in-memory cache for storing and retrieving data.
    """

    def __init__(self):
        self.data = {}
        self.cache_validators = {}

    def set(self, cache_validator, key, value):
        """
        Store a value in the cache with the given key.
        """
        self.cache_validators[key] = cache_validator
        self.data[key] = value

    def get(self, cache_validator, key):
        """
        Retrieve a value from the cache by its key.
        """
        if cache_validator != self.cache_validators.get(key):
            return None

        return self.data.get(key)

    def clear(self):
        """
        Clear the entire cache.
        """
        self.cache_validators.clear()
        self.data.clear()
