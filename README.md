[![Test](https://github.com/StuartHiring/python-test-sebastienhoarau/actions/workflows/test.yml/badge.svg)](https://github.com/StuartHiring/python-test-sebastienhoarau/actions/workflows/test.yml)

:globe_with_meridians: Unique Geohash :globe_with_meridians:
===

<br/>

# Requirements

* make (if not present, `apt install make` on Linux Debian or `brew install make` on Mac)
* the current sources (python-test-sebastienhoarau)

A Makefile provides convenient shortcuts for most tasks.

<br/>

# Setup

Create a dedicated Python virtual environment, ie. with [conda](https://docs.conda.io/en/latest/miniconda.html):

    conda create -n geo-transformer python=3.9 pip

Activate the virtual environment:

    conda activate geo-transformer

Install minimum requirements and package locally with:

    make install

at the root of the project.

<br/>

# Usage

Change directory to `geo_transformer` directory:

    cd geo_transformer

then run:

    python app.py data/test_points.txt.gz

to use the provided sample data and print output to the console.

You can also use any file respecting the same schema as the one provided, compressed in GZ format for the `INPUT_FILE` argument.

<br/>

List all available commands with:

    python app.py --help

<br/>

# Project structure

```
python-test-sebastienhoarau
├── LICENSE
├── Makefile
├── README.md            # this file
├── geo_transformer      # main package
│   ├── __init__.py
│   ├── app.py           # application entrypoint
│   ├── data             # sample application data
│   ├── io.py            # input/output functions
│   ├── models.py        # datas structures
│   ├── tests            # tests
│   └── transformer.py   # transformer functions (geohash encoding, unique prefix)
├── pyproject.toml
├── requirements-dev.in  # dev requirements
├── requirements-dev.txt # compiled dev requirements with pip-compile
├── requirements.in      # requirements
├── requirements.txt     # compiled requirements with pip-compile
└── setup.py
```

Python source code is formatted with [Black](https://github.com/psf/black).

<br/>

# Development environment

Similar to [Setup](#setup), while at the root of the project, install development requirements and package locally with:

`make install-dev`.

<br/>

# Run tests

Tests can be run with:

`make test`

The console prints tests outputs as well as code coverage.

<br/>

# Updating dependencies

The requirements files `requirements.txt` and `requirements-dev.txt` are generated with `pip-compile` from [pip-tools](https://github.com/jazzband/pip-tools). 

* update `requirements.in` and `requirements-dev.in` as needed
* run `pip-compile requirements.in` and `pip-compile requirements-dev.in` to update the compiled requirements.

<br/>

# Original Problem Statement

Your task is to transform the set of longitude, latitude coordinates provided in the `test_points.txt.gz` file
into corresponding [GeoHash](https://en.wikipedia.org/wiki/Geohash) codes.
For each pair of coordinates only the shortest geohash prefix that uniquely identifies this point must be stored.
For instance, this 3 points dataset will store these unique prefixes:

|latitude        | longitude       | geohash      | unique_prefix |
|----------------|-----------------|--------------|---------------|
|41.388828145321 | 2.1689976634898 | sp3e3qe7mkcb | sp3e3         |
|41.390743       | 2.138067        | sp3e2wuys9dr | sp3e2wuy      |
|41.390853       | 2.138177        | sp3e2wuzpnhr | sp3e2wuz      |

The solution must be coded in `Python` and you can use any public domain libraries.
It should work with any file respecting the same schema as the one provided.
The executable must output the solution on `stdout` in [CSV format](https://tools.ietf.org/html/rfc4180)
with 4 columns following the structure of the example, *ie*:

```csv
lat,lng,geohash,uniq
41.388828145321,2.1689976634898,sp3e3qe7mkcb,sp3e3
41.390743,2.138067,sp3e2wuys9dr,sp3e2wuy
41.390853,2.138177,sp3e2wuzpnhr,sp3e2wuz
```

<br/>

## :nerd_face: We value in the solution

- Good software design
- Proper documentation
- Compliance to Python standards and modern usages (*eg.*: [PEP8](https://www.python.org/dev/peps/pep-0008/))
- Proper use of data structures
- Ergonomy of the command line interface
- Setup/Launch instructions if required
