from geolib import geohash as geohashlib
from geo_transformer.models import Geohash, Location
from typing import Generator


def encode(latitude: float, longitude: float, precision: int = 12) -> str:
    """Encode latitude and longitude to geohash.

    Args:
        latitude (float): latitude of a given location
        longitude (float): longitude of a given location
        precision (int, optional): geohash prevision, from 1 (lowest) to 12 (highest), included. Defaults to 12.

    Returns:
        str: geohash as string
    """
    geohash = geohashlib.encode(latitude, longitude, precision)
    return geohash


def transform(locations: Generator[Location, None, None]) -> Generator[Geohash, None, None]:
    """transform locations to geohashs. Adds geohash encoding and a unique prefix identifier to input locations.

    Args:
        locations (Generator[Location, None, None]): Locations to transform

    Yields:
        Generator[Geohash, None, None]: GeoHash objects
    """
    geohashs = (Geohash(location=location, geohash=encode(location.lat, location.lng), uniq="") for location in locations)
    return geohashs
