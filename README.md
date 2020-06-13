# Create aio app

[![Build Status](https://travis-ci.com/aio-libs/create-aio-app.svg?branch=master)](https://travis-ci.com/aio-libs/create-aio-app)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Gitter chat](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/aio-libs/Lobby)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-green.svg)](https://github.com/aio-libs/create-aio-app/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22)
[![PyPI version](https://badge.fury.io/py/create-aio-app.svg)](https://badge.fury.io/py/create-aio-app)

The tool that lets you bootstrap aiohttp application with best practices ready for development.

![Example](https://raw.githubusercontent.com/aio-libs/create-aio-app/master/assets/assets.png)

## Installation

Requires python3.6 - python3.7 and docker-compose

```bash
pip install create-aio-app
```

## Usage

```bash
create-aio-app my_project
```

If you want to use interactive mode enter the next command:

```bash
create-aio-app
```

This will create a new directory called `my_project`.
To start you new project run the next commands:

```bash
cd my_project

make run # start your project
```

[Here is a link to all the make commands.](https://create-aio-app.readthedocs.io/pages/commands.html)


Then, navigate in your browser to `http://localhost:8080/`

## Features

- [aiohttp](https://aiohttp.readthedocs.io/en/stable/) - the best python framework :)
- [mypy](https://mypy.readthedocs.io/en/latest/) - optional static typing
- [pytest](https://pytest.readthedocs.io/en/latest/) - unit tests
- [flake8](https://flake8.readthedocs.io/en/latest/) - linter
- [black](https://black.readthedocs.io/en/latest/) - code formatter
- [trafaret](https://trafaret.readthedocs.io/en/latest/) - data validation
- [aio devtools](https://github.com/aio-libs/aiohttp-devtools) - developer tools
- [aiohttp debug toolbar](https://github.com/aio-libs/aiohttp-debugtoolbar) - tool for debugging
- [postgres](https://www.postgresql.org/) - storage
- [alembic](https://alembic.sqlalchemy.org/en/latest/tutorial.html) - database migration tool
- [sqlAlchemy](https://www.sqlalchemy.org/) - orm
- [sphinx](http://www.sphinx-doc.org/en/master/) - docs
- [docker-compose](https://docs.docker.com/compose/) - tool for defining and running multi-container Docker applications
- [py-spy](https://github.com/benfred/py-spy) - Sampling profiler for Python programs

## Options

`--without-postgres` - remove postgres and all of its requirements

`--redis` - add redis to the template

`--uvloop` - uvloop event loop for aiohttp

## Contributing

`create-aio-app` is a boilerplate from aiohttp community for aiohttp 
community. Feel free to make any suggestions on the issues or 
create a pull request. We will be very happy 😀. 
See [CONTRIBUTING.md](https://github.com/aio-libs/create-aio-app/blob/master/CONTRIBUTING.md) for more information about 
how to contribute to `create-aio-app`.

## License

Create aio App is an open source software <a href="https://github.com/aio-libs/create-aio-app/blob/master/LICENSE">available under the MIT license</a>.
