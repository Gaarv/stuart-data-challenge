from typing import NamedTuple


class Location(NamedTuple):
    lat: float
    lng: float


class Geohash(NamedTuple):
    location: Location
    geohash: str
    uniq: str
