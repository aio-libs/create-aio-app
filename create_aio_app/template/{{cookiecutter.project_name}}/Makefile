export PYTHONPATH=.

PROJECT_NAME={{ cookiecutter.project_name }}

# Common

all: run

run:
	@docker-compose up {{ cookiecutter.project_name }}_app

stop:
	@docker-compose stop

clean:
	@docker-compose down

bash:
	@docker exec -it {{ cookiecutter.project_name }} bash

# Linters & tests

mypy:
	@docker-compose run --rm $(PROJECT_NAME)_app mypy $(PROJECT_NAME)

lint:
	@docker-compose run --rm $(PROJECT_NAME)_app flake8 $(PROJECT_NAME)

_test:
	# todo: remove no:warnings
	@py.test -p no:warnings --cov

test: lint
	@docker-compose up test
	@docker-compose stop test

{%- if cookiecutter.use_postgres == 'y' %}
# Database

psql:
	@docker exec -it {{ cookiecutter.project_name }}_postgres psql -U postgres

migrations:
	@docker exec -it {{ cookiecutter.project_name }} alembic -n alembic:dev revision --autogenerate;

migrate:
	@docker exec -it {{ cookiecutter.project_name }} alembic -n alembic:dev upgrade head;
{%- endif %}

run_production:
	@docker-compose -f docker-compose.yml -f docker-compose.production.yml up
