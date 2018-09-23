# Create aio app

[![Python Versions][pyversion-button]][md-pypi]
[![Latest Version][mdversion-button]][md-pypi]
[![BSD License][bsdlicense-button]][mitlicense]

The tool that helps quickly create a basis for the microservice on aiohttp and prepare the development environment.

![Example](assets/assets.png)

## Installation

Requires python3.5 - python3.7 and docker-compose

```bash
pip install create-aio-app
```

## Usage

```bash

create-aio-app my_project
```

After that it will create new directory `my_project`.

```bash
cd my_project

make run # start your project
```

and open in your browser `http://localhost:8080/`

## Features

- aiohttp
- mypy
- pytest
- flake8
- trafaret
- docker-compose
- aio devtools
- aiohttp debug toolbar
- postgres
- alembic
- aiopg
- sqlAlchemy


## Options

`--without-postgres` - remove postgres and all helpful libs connected with db from template

`--redis` - add redis to the template

