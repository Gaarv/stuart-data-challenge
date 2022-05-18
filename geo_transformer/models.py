from typing import NamedTuple


class Location(NamedTuple):
    """A location represented by latitude and longitude."""

    lat: float
    lng: float


class Geohash(NamedTuple):
    """A object containing original location, geohash encoding and a unique prefix identifier."""

    location: Location
    geohash: str
    uniq: str
