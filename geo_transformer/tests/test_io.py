import tempfile
from pathlib import Path
from typing import Generator

from geo_transformer.io import extract_from_file, load_locations, write_to_file
from geo_transformer.models import Location
from geo_transformer.tests.conftest import TEST_FILE, EXPECTED_TEST_OUTPUT
from geo_transformer import transformer


def test_extract_from_file():
    extracted_file = extract_from_file(TEST_FILE)
    assert extracted_file is not None
    assert extracted_file.exists()
    assert len(extracted_file.open("r").readlines()) == 4


def test_extract_from_non_existing_file():
    extracted_file = extract_from_file(Path("/path/to/nofile.gz"))
    assert extracted_file is None


def test_extract_from_non_gzip_file():
    with tempfile.NamedTemporaryFile(suffix=".gz") as test_file:
        extracted_file = extract_from_file(Path(test_file.name))
        assert extracted_file is None


def test_load_points(extracted_file):
    data_points = load_locations(extracted_file)
    assert len(list(data_points)) == 3


def test_write_to_file(data_test_locations: Generator[Location, None, None]):
    with tempfile.NamedTemporaryFile(suffix=".csv") as output_file:
        locations = list(data_test_locations)  # copy generator to list
        index = transformer.build(transformer.encode(location.lat, location.lng) for location in locations)
        geohashs = transformer.transform(locations, index)  # type: ignore
        write_to_file(Path(output_file.name), geohashs)
        assert Path(output_file.name).read_text() == EXPECTED_TEST_OUTPUT
