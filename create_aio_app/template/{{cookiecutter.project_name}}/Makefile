PROJECT_NAME={{ cookiecutter.project_name }}

# colors
GREEN = $(shell tput -Txterm setaf 2)
YELLOW = $(shell tput -Txterm setaf 3)
WHITE = $(shell tput -Txterm setaf 7)
RESET = $(shell tput -Txterm sgr0)
GRAY = $(shell tput -Txterm setaf 6)
TARGET_MAX_CHAR_NUM = 20

# Common

all: run

## Runs application. Builds, creates, starts, and attaches to containers for a service. | Common
run:
	@docker-compose up $(PROJECT_NAME)_app

## Rebuild {{ cookiecutter.project_name }}_app container
build:
	@docker-compose build $(PROJECT_NAME)_app

## Stops application. Stops running container without removing them.
stop:
	@docker-compose stop

## Removes stopped service containers.
clean:
	@docker-compose down

## Runs command `bash` commands in docker container.
bash:
	@docker exec -it $(PROJECT_NAME) bash

## Upgrade your python's dependencies:
upgrade:
	docker-compose run --rm $(PROJECT_NAME)_app python3 -m $(PROJECT_NAME).utils.check-requirements

# Help

## Shows help.
help:
	@echo ''
	@echo 'Usage:'
	@echo ''
	@echo '  ${YELLOW}make${RESET} ${GREEN}<target>${RESET}'
	@echo ''
	@echo 'Targets:'
	@awk '/^[a-zA-Z\-\_]+:/ { \
		helpMessage = match(lastLine, /^## (.*)/); \
		if (helpMessage) { \
		    if (index(lastLine, "|") != 0) { \
				stage = substr(lastLine, index(lastLine, "|") + 1); \
				printf "\n ${GRAY}%s: \n\n", stage;  \
			} \
			helpCommand = substr($$1, 0, index($$1, ":")-1); \
			helpMessage = substr(lastLine, RSTART + 3, RLENGTH); \
			if (index(lastLine, "|") != 0) { \
				helpMessage = substr(helpMessage, 0, index(helpMessage, "|")-1); \
			} \
			printf "  ${YELLOW}%-$(TARGET_MAX_CHAR_NUM)s${RESET} ${GREEN}%s${RESET}\n", helpCommand, helpMessage; \
		} \
	} \
	{ lastLine = $$0 }' $(MAKEFILE_LIST)
	@echo ''

# Docs

## Generate html documentation. | Documentation
doc:
	@docker-compose run --rm $(PROJECT_NAME)_app make _doc

_doc:
	@doc8 docs
	@cd docs && make html

# Linters & tests

## Formats code with `black`. | Linters
black:
	@docker-compose run --rm $(PROJECT_NAME)_app black $(PROJECT_NAME) --exclude $(PROJECT_NAME)/migrations -l 79

## Checks types with `mypy`.
mypy:
	@docker-compose run --rm $(PROJECT_NAME)_app mypy $(PROJECT_NAME)

## Formats code with `flake8`.
lint:
	@docker-compose run --rm $(PROJECT_NAME)_app flake8 $(PROJECT_NAME)

## Runs tests. | Tests
test: lint
	@docker-compose up test
	@docker-compose stop test

{%- if cookiecutter.use_postgres == 'y' %}
# Database

## Runs PostgreSQL UI. | Database
psql:
	@docker exec -it $(PROJECT_NAME)_postgres psql -U postgres

## Makes migration.
migrations:
	@docker exec -it $(PROJECT_NAME) alembic -n alembic:dev revision --autogenerate;

## Upgrades database.
migrate:
	@docker exec -it $(PROJECT_NAME) alembic -n alembic:dev upgrade head;

{%- endif %}

## Runs application with development config.
adev: {%- if cookiecutter.use_postgres == 'y' or cookiecutter.use_redis == 'y' %} wait_resources {% endif %}
	adev runserver ./$(PROJECT_NAME)/__main__.py -p 8080


{%- if cookiecutter.use_postgres == 'y' or cookiecutter.use_redis == 'y' %}

## Runs application with specified postgres and redis.
wait_resources:
	python3 -m $(PROJECT_NAME).utils.wait_script
{%- endif %}
