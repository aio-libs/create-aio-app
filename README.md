# Create aio app
[![Build Status](https://travis-ci.com/aio-libs/create-aio-app.svg?branch=master)](https://travis-ci.com/aio-libs/create-aio-app)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Gitter chat](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/aio-libs/Lobby)

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

or if u wanna use manual mode, enter only command below

```bash
create-aio-app
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


## License

Create aio App is open source software <a href="https://github.com/aio-libs/create-aio-app/blob/master/LICENSE">licensed as MIT</a>. 
