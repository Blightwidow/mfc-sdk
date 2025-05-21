import inspect
from dataclasses import dataclass
from typing import Self

from mfc.client.myflyclub import mfc_client


@dataclass
class Feature:
    """Class representing a feature of an airport.

    Attributes:
        title (str): Title of the feature.
        strength (int): Strength of the feature.
        type (str): Type of the feature.
    """

    title: str
    strength: int
    type: str


@dataclass
class Airport:
    citiesServed: list[str]  # Seems to be unused
    city: str
    countryCode: str
    destinations: list[Self]
    features: list[Feature]
    iata: str
    icao: str
    id: int
    incomeLevel: int
    latitude: float
    longitude: float
    name: str
    popElite: str
    popMiddleIncome: float
    population: int
    radius: int
    runwayLength: int
    size: int
    zone: str

    championAirlineId: int | None = None
    championAirlineName: str | None = None
    contested: str | None = None
    isGateway: bool | None = False
    isDomesticAirport: bool | None = False

    @classmethod
    def from_dict(cls, env):
        return cls(
            **{k: v for k, v in env.items() if k in inspect.signature(cls).parameters}
        )


def all() -> list[Airport]:
    """Get all airports.
    Returns:
        list[Airport]: A list of all airports.
    """
    raw_airports = mfc_client.get("/airports")
    return [Airport(**airport) for airport in raw_airports]


def id(id: int) -> Airport | None:
    """Get an airport by its ID.

    Args:
        airport_id (int): The ID of the airport.

    Returns:
        Airport | None: The airport object if found, None otherwise.
    """
    airports = all()
    for airport in airports:
        if airport.id == id:
            return airport

    return None
