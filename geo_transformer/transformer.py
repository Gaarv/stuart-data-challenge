from typing import Generator

from geolib import geohash as geohashlib

from geo_transformer.models import Geohash, Location
from geo_transformer.trie import Trie


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


def build(geohashs: Generator[str, None, None]) -> Trie:
    """Helper function to build a trie from a geohash generator.

    Args:
        geohashs (Generator[str, None, None]): list of geohashes to insert into the trie

    Returns:
        Trie: a trie with all geohashes inserted
    """
    trie = Trie()
    for geohash in geohashs:
        trie.insert(geohash)
    return trie


def query_unique_prefix(geohash: str, trie: Trie) -> str:
    """Query a trie to obtain a unique prefix for a given geohash.

    Args:
        geohash (str): geohash to query
        trie (Trie): Trie to query against

    Returns:
        str: unique prefix found in the trie
    """
    unique_index = 0

    # reverse the path found
    reversed_path = trie.search(geohash)[::-1]
    for i in range(len(reversed_path)):
        unique_index = i
        # stop when the parent node of the current child has more than one child
        if len(reversed_path[i + 1].children) > 1:
            break

    # slice the path to obtain the unique prefix and reverse it back
    path = reversed_path[unique_index:][::-1]
    return "".join([node.char for node in path])


def transform(locations: Generator[Location, None, None], trie: Trie) -> Generator[Geohash, None, None]:
    """transform locations to geohashs. Adds geohash encoding and a unique prefix identifier to input locations.

    Args:
        locations (Generator[Location, None, None]): Locations to transform

    Yields:
        Generator[Geohash, None, None]: GeoHash objects
    """
    for location in locations:
        geohash = encode(location.lat, location.lng)
        unique_prefix = query_unique_prefix(geohash, trie)
        yield Geohash(location=location, geohash=geohash, uniq=unique_prefix)
