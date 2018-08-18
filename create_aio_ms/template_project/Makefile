export PYTHONPATH=.

PROJECT_NAME={{name}}

all: run

run:
	@adev runserver $(PROJECT_NAME)/__main__.py

mypy:
	@mypy $(PROJECT_NAME)

lint:
	@flake8 $(PROJECT_NAME)

test: lint
	@py.test
