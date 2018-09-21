# {{ name }}

___

## Requirements
- docker-compose

___

## Local development
All develop settings for application are in the `/config/api.dev.yml`.

### Run
To start the project in develop mode, run the following command:

```bash
make run
```

or just

```bash
make
```

For stop work of docker containers use:

```bash
make stop
```

Interactive work inside container

```bash
make bash # the command must be running after `make run` 
```

### Linters
To run flake8, run the following command:

```bash
make lint
```

The all settings connected with a `flake8` you can customize in `.flake8`.

### Type checking
To run mypy for type checking run the following command:

```bash
make mypy
```

The all settings connected with a `mypy` you can customize in `mypy.ini`.
___

{% if not without_postgres %}

### Testing
```bash
make test
```

### Database
Management of database (postgres) migrations takes place with the help of [alembic](http://alembic.zzzcomputing.com/en/latest/).

Create new migration (new file in `{{name}}/migrations/versions/`):

```bash
make migrations # the command must be running after `make run` 
```

Apply migrations:

```bash
make migrate # the command must be running after `make run` 
```

If u wanna create new file with tables u should import tables to `{{name}}/migrations/env.py`

```bash
import {{ name }}.users.tables
# add new files here
```

If u need to make downgrade or other special things with alembic, use `make bash`
for penetration inside the container and run native alembic's commands.

```bash
make bash
alembic downgrade -1
```

To connect to postgres, use the command below

```bash
make psql # the command must be running after `make run` 
```
{% endif %}

## Production
All production settings for application are in the `/config/api.prod.yml`.

The production and develop containers have a little bit different and all that different describe in docker-compose.production.yml. This  is works with the command bellow:

```bash
make production
```

for more information [docs](https://docs.docker.com/compose/reference/overview/).
___

## Software

- python3.7
- aiohttp
- mypy
