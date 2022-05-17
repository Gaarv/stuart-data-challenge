from pathlib import Path
from typing import Optional

import typer

from geo_transformer import io

app = typer.Typer()


@app.command()
def main(
    input_file: Path = typer.Argument(..., help="Path to input file, GZ compressed."),
    output_file: Optional[Path] = typer.Option(None, help="Path to output file. If not provided, output will be printed to stdout."),
    verbose: bool = typer.Option(False, help="Provide additional information while running the program."),
):
    if input_file.is_file():
        extracted_file = io.extract_from_file(input_file)
        if extracted_file:
            locations = io.load_points(extracted_file)
            if not output_file:
                io.print_to_console(locations)
            else:
                pass
        else:
            raise typer.Exit(code=1)
    else:
        typer.secho(f"Input file {input_file} does  not exist", fg=typer.colors.RED)
        raise typer.Exit(code=1)


if __name__ == "__main__":
    app()
