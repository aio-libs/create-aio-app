export PYTHONPATH=.

PROJECT_NAME={{name}}

all: run

run:
	@docker-compose up

mypy:
	@docker-compose run --rm app mypy $(PROJECT_NAME)

lint:
	@docker-compose run --rm app flake8 $(PROJECT_NAME)

test: lint
	@py.test

run_production:
	@docker-compose -f docker-compose.yml -f docker-compose.production.yml up
