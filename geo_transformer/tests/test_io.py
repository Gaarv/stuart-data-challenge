from geo_transformer.io import extract_from_file, load_locations
from geo_transformer.tests.conftest import TEST_FILE


def test_extract_from_file():
    extracted_file = extract_from_file(TEST_FILE)
    assert extracted_file is not None
    assert extracted_file.exists()
    assert len(extracted_file.open("r").readlines()) == 4


def test_load_points(extracted_file):
    data_points = load_locations(extracted_file)
    assert len(list(data_points)) == 3
