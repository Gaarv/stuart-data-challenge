from typing import Generator

from geo_transformer.models import Geohash, Location
from geo_transformer.transformer import encode


def test_geohash_instance(data_test_locations: Generator[Location, None, None]):
    for location in data_test_locations:
        assert isinstance(Geohash(location=location, geohash=encode(location.lat, location.lng), uniq=""), Geohash)


def test_geohash_encode(data_test_locations: Generator[Location, None, None]):
    geohashs = [encode(location.lat, location.lng) for location in data_test_locations]
    assert geohashs == ["sp3e3qe7mkcb", "sp3e2wuys9dr", "sp3e2wuzpnhr"]


def test_geohash_encode_benchmark(data_test_locations: Generator[Location, None, None], benchmark):
    location = list(data_test_locations)[0]
    geohash = benchmark(encode, location.lat, location.lng)
    assert geohash == "sp3e3qe7mkcb"
