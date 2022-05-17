from pathlib import Path
from typing import Optional

import pytest
from geo_transformer.io import extract_from_file, load_points

TEST_FILE = Path("geo_transformer/tests/data/test_points.txt.gz")


@pytest.fixture(scope="session")
def extracted_file():
    return extract_from_file(TEST_FILE)


@pytest.fixture(scope="function")
def data_test_points(extracted_file: Optional[Path]):
    if extracted_file:
        data_points = load_points(extracted_file)
        return data_points
    else:
        return []
