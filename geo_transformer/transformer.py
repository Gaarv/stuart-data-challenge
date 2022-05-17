from geolib import geohash as geohashlib


def encode(latitude: float, longitude=float, precision: int = 7) -> str:
    geohash = geohashlib.encode(latitude, longitude, precision)
    return geohash
