import random
import string
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


@pytest.mark.benchmark(group="trie-insert")
def test_build_index_benchmark_1_000(benchmark):
    geohashs = generate_fake_random_geohash(1_000)
    benchmark(build, geohashs)


@pytest.mark.benchmark(group="trie-insert")
def test_build_index_benchmark_10_000(benchmark):
    geohashs = generate_fake_random_geohash(10_000)
    benchmark(build, geohashs)


@pytest.mark.benchmark(group="trie-insert")
def test_build_index_benchmark_100_000(benchmark):
    geohashs = generate_fake_random_geohash(100_000)
    benchmark(build, geohashs)


@pytest.mark.benchmark(group="trie-insert")
def test_build_index_benchmark_1_000_000(benchmark):
    geohashs = generate_fake_random_geohash(1_000_000)
    benchmark(build, geohashs)


@pytest.mark.benchmark(group="trie-query")
def test_query_unique_prefix_benchmark_small_trie(data_test_locations: Generator[Location, None, None], benchmark):
    index = build(encode(location.lat, location.lng) for location in data_test_locations)
    prefix = benchmark(query_unique_prefix, "sp3e3qe7mkcb", index)
    assert prefix == "sp3e3"


@pytest.mark.benchmark(group="trie-query")
def test_query_unique_prefix_benchmark_large_trie(benchmark):
    geohashs = generate_fake_random_geohash(1_000_000)
    index = build(geohashs)
    benchmark(query_unique_prefix, generate_fake_random_geohash(1), index)


def generate_fake_random_geohash(size: int) -> Generator[str, None, None]:
    """Generate a fake (invalid) geohash-like of stringof with 12 random characters

    Args:
        size (int): number of fake geohashs to generate

    Yields:
        Generator[str, None, None]: fake geohashs strings
    """
    for _ in range(size):
        yield "".join(random.choice(string.ascii_lowercase) for _ in range(12))
