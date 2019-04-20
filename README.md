# Create aio app
[![Build Status](https://travis-ci.com/aio-libs/create-aio-app.svg?branch=master)](https://travis-ci.com/aio-libs/create-aio-app)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Gitter chat](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/aio-libs/Lobby)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-green.svg)](https://github.com/aio-libs/create-aio-app/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22)

The tool that helps quickly create a basis for the microservice on aiohttp and prepare the development environment.

![Example](https://raw.githubusercontent.com/aio-libs/create-aio-app/master/assets/assets.png)

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

- [aiohttp](https://aiohttp.readthedocs.io/en/stable/) - the best python framework :)
- [mypy](https://mypy.readthedocs.io/en/latest/) - for optional static typing
- [pytest](https://pytest.readthedocs.io/en/latest/) - for run unit tests
- [black](https://black.readthedocs.io/en/latest/) - for code formatter
- [flake8](https://flake8.readthedocs.io/en/latest/) - for linting
- [trafaret](https://trafaret.readthedocs.io/en/latest/) - for validation input data
- [aio devtools](https://github.com/aio-libs/aiohttp-devtools) - helpful tool for develop
- [aiohttp debug toolbar](https://github.com/aio-libs/aiohttp-debugtoolbar) - helpful tool for debugging
- [postgres](https://www.postgresql.org/) - storage
- [alembic](https://alembic.sqlalchemy.org/en/latest/tutorial.html) - tool for create migration
- [sqlAlchemy](https://www.sqlalchemy.org/) - orm
- [sphinx](http://www.sphinx-doc.org/en/master/) - for generate docs
- [docker-compose](https://docs.docker.com/compose/) - for running develop environment and deploy




## Options

`--without-postgres` - remove postgres and all helpful libs connected with db from template

`--redis` - add redis to the template

`--uvloop` - use uvloop event loop for aiohttp

## Contributing
The `create-aio-app` it's a boilerplate from aiohttp community for aiohttp 
community. So, feel free to make some suggestion in the issue or make 
pull requests. We will be happy 😀. See [CONTRIBUTING.md](https://github.com/aio-libs/create-aio-app/blob/master/CONTRIBUTING.md) for more information about 
how to contribute to `create-aio-app`.

## License

Create aio App is an open source software <a href="https://github.com/aio-libs/create-aio-app/blob/master/LICENSE">available under the MIT license</a>. 
