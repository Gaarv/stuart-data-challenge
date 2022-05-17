from typing import Generator

import pytest
from geo_transformer.models import Geohash, Location
from geo_transformer.transformer import build, encode, query_unique_prefix, transform


def test_geohash_instance(data_test_locations: Generator[Location, None, None]):
    for location in data_test_locations:
        assert isinstance(Geohash(location=location, geohash=encode(location.lat, location.lng), uniq=""), Geohash)


def test_geohash_encode(data_test_locations: Generator[Location, None, None]):
    geohashs = [encode(location.lat, location.lng) for location in data_test_locations]
    assert geohashs == ["sp3e3qe7mkcb", "sp3e2wuys9dr", "sp3e2wuzpnhr"]


def test_query_unique_prefix(data_test_locations: Generator[Location, None, None]):
    index = build(encode(location.lat, location.lng) for location in data_test_locations)
    prefix = query_unique_prefix("sp3e3qe7mkcb", index)
    assert prefix == "sp3e3"


def test_transformer(data_test_locations: Generator[Location, None, None]):
    locations = list(data_test_locations)  # copy generator to list
    index = build(encode(location.lat, location.lng) for location in locations)
    results = transform(locations, index)  # type: ignore
    prefixes = [geohash.uniq for geohash in results]
    assert len(list(prefixes)) == 3
    assert prefixes == ["sp3e3", "sp3e2wuy", "sp3e2wuz"]


@pytest.mark.benchmark(group="geohash")
def test_geohash_encode_benchmark(data_test_locations: Generator[Location, None, None], benchmark):
    location = list(data_test_locations)[0]
    geohash = benchmark(encode, location.lat, location.lng)
    assert geohash == "sp3e3qe7mkcb"


@pytest.mark.benchmark(group="trie")
def test_query_unique_prefix_benchmark(data_test_locations: Generator[Location, None, None], benchmark):
    index = build(encode(location.lat, location.lng) for location in data_test_locations)
    prefix = benchmark(query_unique_prefix, "sp3e3qe7mkcb", index)
    assert prefix == "sp3e3"
