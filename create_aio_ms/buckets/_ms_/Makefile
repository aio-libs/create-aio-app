export PYTHONPATH=.

PROJECT_NAME=_ms_

all: run

run:
	@python -m $(PROJECT_NAME)

mypy:
	@mypy $(PROJECT_NAME)

lint:
	@flake8 $(PROJECT_NAME)

test: lint
	@py.test

start_database:
	@docker-compose up -d postgres
