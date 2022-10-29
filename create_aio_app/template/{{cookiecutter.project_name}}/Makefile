PROJECT_NAME={{ cookiecutter.project_name }}
TIME=60
SUPPORTED_COMMANDS := all run build stop clean bash upgrade profile help doc black mpy lint test psql migrations migrate adev wait_resources
SUPPORTS_MAKE_ARGS := $(findstring $(firstword $(MAKECMDGOALS)), $(SUPPORTED_COMMANDS))
ifneq "$(SUPPORTS_MAKE_ARGS)" ""
  COMMAND_ARGS := $(wordlist 2,$(words $(MAKECMDGOALS)),$(MAKECMDGOALS))
	MAKEFILE_PATH := $(abspath $(firstword $(MAKEFILE_LIST)))
  $(eval $(COMMAND_ARGS):;@:)
endif

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
	@docker-compose up $(PROJECT_NAME)_app $(COMMAND_ARGS)

## Rebuild {{ cookiecutter.project_name }}_app container
build:
	@docker-compose build $(PROJECT_NAME)_app $(COMMAND_ARGS)

## Stops application. Stops running container without removing them.
stop:
	@docker-compose stop $(COMMAND_ARGS)

## Removes stopped service containers.
clean:
	@docker-compose down $(COMMAND_ARGS)

## Runs command `bash` commands in docker container.
bash:
	@docker exec -it $(PROJECT_NAME) bash $(COMMAND_ARGS)

## Upgrade your python's dependencies:
upgrade:
	docker-compose run --rm $(PROJECT_NAME)_app python3 -m $(PROJECT_NAME).utils.check-requirements $(COMMAND_ARGS)

## Create profile sampling of application.
profile:
	@docker exec -it $(PROJECT_NAME) py-spy record -d $(TIME) -o $(PROJECT_NAME)_profile.svg --pid 7 $(COMMAND_ARGS)

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
	@docker-compose run --rm $(PROJECT_NAME)_app make _doc $(COMMAND_ARGS)

_doc:
	@doc8 docs
	@cd docs && make html

# Linters & tests

## Formats code with `black`. | Linters
black:
	@docker-compose run --rm $(PROJECT_NAME)_app black $(PROJECT_NAME) --exclude $(PROJECT_NAME)/migrations -l 79 $(COMMAND_ARGS)

## Checks types with `mypy`.
mypy:
	@docker-compose run --rm $(PROJECT_NAME)_app mypy $(PROJECT_NAME) $(COMMAND_ARGS)

## Formats code with `flake8`.
lint:
	@docker-compose run --rm $(PROJECT_NAME)_app flake8 $(PROJECT_NAME) $(COMMAND_ARGS)

## Runs tests. | Tests
test: lint
	@docker-compose up test
	@docker-compose stop test

{%- if cookiecutter.use_postgres == 'y' %}
# Database

## Runs PostgreSQL UI. | Database
psql:
	@docker exec -it $(PROJECT_NAME)_postgres psql -U postgres $(COMMAND_ARGS)

## Makes migration.
migrations:
	@docker exec -it $(PROJECT_NAME) alembic -n alembic:dev revision --autogenerate $(COMMAND_ARGS);

## Upgrades database.
migrate:
	@docker exec -it $(PROJECT_NAME) alembic -n alembic:dev upgrade head $(COMMAND_ARGS);

{%- endif %}

## Runs application with development config.
adev: {%- if cookiecutter.use_postgres == 'y' or cookiecutter.use_redis == 'y' %} wait_resources {% endif %}
	adev runserver ./$(PROJECT_NAME)/__main__.py -p 8080


{%- if cookiecutter.use_postgres == 'y' or cookiecutter.use_redis == 'y' %}

## Runs application with specified postgres and redis.
wait_resources:
	python3 -m $(PROJECT_NAME).utils.wait_script
{%- endif %}
