from geo_transformer.app import app
from geo_transformer.tests.conftest import TEST_FILE
from typer.testing import CliRunner

runner = CliRunner()


def test_app():
    result = runner.invoke(app, [TEST_FILE.as_posix()])
    assert result.exit_code == 0
    assert "lat,lng,geohash,uniq" in result.stdout
    assert "41.388828145321,2.1689976634898" in result.stdout
    assert "41.390743,2.138067" in result.stdout
    assert "41.390853,2.138177" in result.stdout
    assert "sp3e3qe7mkcb" in result.stdout
    assert "sp3e2wuys9dr" in result.stdout
    assert "sp3e2wuzpnhr" in result.stdout
    assert "sp3e3" in result.stdout
    assert "sp3e2wuy" in result.stdout
    assert "sp3e2wuz" in result.stdout
