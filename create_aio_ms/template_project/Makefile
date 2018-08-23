export PYTHONPATH=.

PROJECT_NAME={{name}}

all: run

run:
	@docker-compose up
	# docker-compose run --rm app echo 1

mypy:
	@mypy $(PROJECT_NAME)

lint:
	@flake8 $(PROJECT_NAME)

test: lint
	@py.test

run_production:
	@docker-compose -f docker-compose.yml -f docker-compose.production.yml up
