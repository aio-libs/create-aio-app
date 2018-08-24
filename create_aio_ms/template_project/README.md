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
