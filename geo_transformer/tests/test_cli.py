import tempfile
from pathlib import Path

from geo_transformer.app import app
from geo_transformer.tests.conftest import EXPECTED_TEST_OUTPUT, TEST_FILE
from typer.testing import CliRunner

runner = CliRunner()


def test_app_stdout():
    result = runner.invoke(app, [TEST_FILE.as_posix()])
    assert result.exit_code == 0
    assert result.output == EXPECTED_TEST_OUTPUT


def test_app_output_to_file():
    with tempfile.NamedTemporaryFile(suffix=".csv") as output_file:
        result = runner.invoke(app, [TEST_FILE.as_posix(), "--output-file", output_file.name])
        assert result.exit_code == 0
        assert Path(output_file.name).read_text() == EXPECTED_TEST_OUTPUT


def test_app_non_existing_file():
    test_file = "non_existing_file.csv"
    result = runner.invoke(app, [test_file])
    assert result.exit_code == 1
    assert result.output == f"Input file {test_file} does not exist\n"


def test_app_non_gz_file():
    with tempfile.NamedTemporaryFile(suffix=".gz") as test_file:
        result = runner.invoke(app, [test_file.name])
        assert result.exit_code == 1
        assert result.output == f"Error while extracting archive {test_file.name}: Input file {test_file.name} is not a valid gzip file\n"
