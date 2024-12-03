all: lint test clean

lint:
	ruff check --select I --fix
	ruff format
	ruff check

test:
	pytest

clean:
	find . -type d -name __pycache__ | xargs rm -rf
	find . -type d -name .pytest_cache | xargs rm -rf
	find . -type d -name .ruff_cache | xargs rm -rf