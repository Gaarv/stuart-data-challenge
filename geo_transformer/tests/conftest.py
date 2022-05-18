from pathlib import Path
from typing import Optional

import pytest
from geo_transformer.io import extract_from_file, load_locations

TEST_FILE = Path("geo_transformer/tests/data/test_points.txt.gz")


EXPECTED_TEST_OUTPUT = """lat,lng,geohash,uniq
41.388828145321,2.1689976634898,sp3e3qe7mkcb,sp3e3
41.390743,2.138067,sp3e2wuys9dr,sp3e2wuy
41.390853,2.138177,sp3e2wuzpnhr,sp3e2wuz
"""


@pytest.fixture(scope="session")
def extracted_file():
    return extract_from_file(TEST_FILE)


@pytest.fixture(scope="function")
def data_test_locations(extracted_file: Optional[Path]):
    if extracted_file:
        data_points = load_locations(extracted_file)
        return data_points
    else:
        return []
