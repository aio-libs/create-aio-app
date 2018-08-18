export PYTHONPATH=.

PROJECT_NAME={{template_project}}

all: run

run:
	@adev runserver $(PROJECT_NAME)/__main__.py

mypy:
	@mypy $(PROJECT_NAME)

lint:
	@flake8 $(PROJECT_NAME)

test: lint
	@py.test
