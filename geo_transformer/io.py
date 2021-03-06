import csv
import gzip
import tempfile
from pathlib import Path
from typing import Generator, Optional

import typer

from geo_transformer.models import Geohash, Location

GZIP_MAGIC_BYTES = "1f8b"
CSV_HEADER = ["lat", "lng", "geohash", "uniq"]


def extract_from_file(archive: Path) -> Optional[Path]:
    """Extract gzip file containing raw data

    Args:
        archive (Path): path to the archive, ie. "data/input.gz"

    Returns:
        Path: extracted file absolute path
    """
    extracted_file = None
    try:
        magic_bytes = archive.open("rb").read(2).hex()
        if magic_bytes != GZIP_MAGIC_BYTES:
            raise Exception(f"Input file {archive.as_posix()} is not a valid gzip file")
        dest = Path(tempfile.mkdtemp()).joinpath(archive.stem)
        content = gzip.decompress(archive.open("rb").read())
        dest.write_bytes(content)
        extracted_file = dest
    except Exception as e:
        typer.secho(f"Error while extracting archive {archive.as_posix()}: {e}", fg=typer.colors.RED, err=True)
    return extracted_file


def load_locations(csv_file: Path) -> Generator[Location, None, None]:
    """Load points from CSV file as Location objects

    Args:
        csv_file (Path): path to the CSV file, ie. "data/input.csv"

    Yields:
        Generator[Location, None, None]: Location objects
    """
    try:
        with csv_file.open("r") as csvfile:
            csvreader = csv.reader(csvfile)
            next(csvreader)  # skip header
            for row in csvreader:
                yield Location(lat=float(row[0]), lng=float(row[1]))
    except Exception as e:
        typer.secho(f"Error while loading points: {e}", fg=typer.colors.RED, err=True)
        yield from ()


def print_to_console(geohashs: Generator[Geohash, None, None]) -> None:
    """Print Geohash objects to console as CSV

    Args:
        locations (Generator[Geohash, None, None]): Geohash objects
    """
    typer.echo(",".join(CSV_HEADER))  # print header
    for geohash in geohashs:
        typer.secho(f"{geohash.location.lat},{geohash.location.lng},{geohash.geohash},{geohash.uniq}")


def write_to_file(output_file: Path, geohashs: Generator[Geohash, None, None]) -> None:
    """Write Geohash objects to CSV file

    Args:
        output_file (Path): path to the output file, ie. "data/output.csv"
        geohashs (Generator[Geohash, None, None]): Geohash objects
    """
    with output_file.open("w") as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(CSV_HEADER)
        for geohash in geohashs:
            csvwriter.writerow([geohash.location.lat, geohash.location.lng, geohash.geohash, geohash.uniq])
