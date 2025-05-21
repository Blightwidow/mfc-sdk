from dataclasses import dataclass
from typing import Self

from mfc.client.myflyclub import mfc_client


@dataclass
class Feature:
    """Class representing a feature of an airport."""

    strength: int
    title: str
    type: str

@dataclass
class AirportDestination:
    """Class representing a destination airport."""

    id: int
    name: str
    countryCode: str
    strength: int
    type: str


@dataclass
class Airport:
    """Class representing an airport."""

    championAirlineId: int | None
    championAirlineName: str | None
    contestingAirlineName: str | None
    countryCode: str
    destinations: list[AirportDestination]
    features: list[Feature]
    iata: str
    icao: str
    id: int
    incomeLevel: int
    isDomesticAirport: bool | None
    isGateway: bool | None
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


def all() -> list[Airport]:
    """Get all airports.
    Returns:
        list[Airport]: A list of all airports.
    """
    raw_airports = mfc_client.get("/airports")
    return [
        Airport(
            id=airport.get("id"),
            countryCode=airport.get("countryCode"),
            destinations=[
                AirportDestination(
                    id=destination.get("id"),
                    name=destination.get("name"),
                    countryCode=destination.get("countryCode"),
                    strength=destination.get("strength"),
                    type=destination.get("type"),
                )
                for destination in airport.get("destinations", [])
            ],
            features=[
                Feature(
                    strength=feature.get("strength"),
                    title=feature.get("title"),
                    type=feature.get("type"),
                )
                for feature in airport.get("features", [])
            ],
            iata=airport.get("iata"),
            icao=airport.get("icao"),
            incomeLevel=airport.get("incomeLevel"),
            latitude=airport.get("latitude"),
            longitude=airport.get("longitude"),
            name=airport.get("name"),
            popElite=airport.get("popElite"),
            popMiddleIncome=airport.get("popMiddleIncome"),
            population=airport.get("population"),
            radius=airport.get("radius"),
            runwayLength=airport.get("runwayLength"),
            size=airport.get("size"),
            zone=airport.get("zone"),
            championAirlineId=airport.get("championAirlineId"),
            championAirlineName=airport.get("championAirlineName"),
            contestingAirlineName=airport.get("contested"),
            isGateway=airport.get("isGateway", False),
            isDomesticAirport=airport.get("isDomesticAirport", False),
        )
        for airport in raw_airports
    ]


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
