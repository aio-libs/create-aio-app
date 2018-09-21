export PYTHONPATH=.

PROJECT_NAME={{name}}

all: run

run:
	@docker-compose up

mypy:
	@docker-compose run --rm $(PROJECT_NAME)_app mypy $(PROJECT_NAME)

lint:
	@docker-compose run --rm $(PROJECT_NAME)_app flake8 $(PROJECT_NAME)

_test:
	@py.test

test: lint
	@docker-compose up test
	@docker-compose stop test

stop:
	@docker-compose stop

bash:
	@docker exec -it {{ name }} bash
{% if not without_postgres %}
# Database
psql:
	@docker exec -it {{ name }}_postgres psql -U postgres

migrations:
	@docker exec -it {{ name }} alembic -n alembic:dev revision --autogenerate;

migrate:
	@docker exec -it {{ name }} alembic -n alembic:dev upgrade head;
{% endif %}
run_production:
	@docker-compose -f docker-compose.yml -f docker-compose.production.yml up
