.PHONY: all

install:
	pip install -r requirements.txt
	pip install -U .

install-dev:
	pip install -r requirements-dev.txt
	pip install -U .

test:
	python -m pytest --cov -v -s -k "not benchmark"

benchmark:
	python -m pytest --cov -v -s -k "benchmark"

profile:
