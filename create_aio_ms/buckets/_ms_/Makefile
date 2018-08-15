export PYTHONPATH=.

PROJECT_NAME=_ms_

all: run

run:
	@adev runserver $(PROJECT_NAME)

mypy:
	@mypy $(PROJECT_NAME)

lint:
	@flake8 $(PROJECT_NAME)

test: lint
	@py.test
