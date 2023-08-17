# Create aio app


[![Build Status](https://travis-ci.com/aio-libs/create-aio-app.svg?branch=master)](https://travis-ci.com/aio-libs/create-aio-app)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Gitter chat](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/aio-libs/Lobby)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-green.svg)](https://github.com/aio-libs/create-aio-app/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22)
[![PyPI version](https://badge.fury.io/py/create-aio-app.svg)](https://badge.fury.io/py/create-aio-app)

The tool that lets you bootstrap aiohttp application with best practices ready for development.

**Here is a screenshot of our interfaces**
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

## Salient Features

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


 # Articles
---

## Simplify Your aiohttp Application Development with Create aio app

Are you looking to kickstart your aiohttp application development while following best practices? Look no further than `create-aio-app`! This powerful tool is designed to help you bootstrap aiohttp applications with ease, setting you up for efficient and structured development right from the start.

**Streamlined Setup Process**

`create-aio-app` simplifies the process of creating a new aiohttp project. With just a single command, you can generate a project structure that adheres to best practices and includes all the necessary components to get you started.

**Interactive Mode for Flexibility**

If you prefer a more interactive approach, `create-aio-app` has got you covered. Enter the command without any arguments, and the tool will guide you through the setup process step by step, allowing you to configure various options along the way.

**A Screenshot Worth a Thousand Words**

To give you a sneak peek into what you can expect, `create-aio-app` provides an interface screenshot that showcases the structure and components of the generated project. This visual representation helps you understand the initial setup at a glance.

**Feature-Rich Development Stack**

`create-aio-app` comes packed with a plethora of features that make it an ideal choice for your aiohttp projects:

- **aiohttp Framework**: The foundation of your application, aiohttp is a robust and high-performance Python web framework that allows you to build asynchronous web applications effortlessly.

- **Optional Static Typing with mypy**: Ensure code correctness and improve maintainability by incorporating optional static typing using the popular `mypy` tool.

- **Unit Testing with pytest**: Create comprehensive unit tests using `pytest` to verify the functionality of your code and catch any issues early in the development process.

- **Code Formatting with black**: Maintain consistent and readable code using `black`, a code formatter that automatically formats your code according to Python's style guide.

- **Linter Support with flake8**: Detect and fix code style and syntax errors using `flake8`, a powerful linter for Python code.

- **Data Validation with trafaret**: Implement data validation effortlessly with `trafaret`, ensuring that your application processes data accurately.

- **Developer Tools and Debugging**: Leverage `aio devtools` and `aiohttp debug toolbar` to enhance your debugging experience and streamline development.

- **Database Integration**: `create-aio-app` supports `postgres` for data storage, along with `alembic` for database migrations and `sqlAlchemy` for object-relational mapping.

- **Documentation with sphinx**: Generate comprehensive documentation for your project using `sphinx`, making it easier for developers to understand and contribute to your codebase.

- **Docker Support with docker-compose**: Define and manage multi-container Docker applications seamlessly using `docker-compose`.

- **Profiling with py-spy**: Identify performance bottlenecks and optimize your application using the `py-spy` sampling profiler.

**Customization Options**

`create-aio-app` also provides customization options to suit your project's specific requirements:

- `--without-postgres`: Remove postgres and its requirements if not needed for your project.
  
- `--redis`: Add redis to the template for integrating a Redis database.
  
- `--uvloop`: Opt for the `uvloop` event loop for aiohttp, enhancing the performance of your asynchronous application.

**Community-Driven and Open Source**

`create-aio-app` is a collaborative effort from the aiohttp community for the aiohttp community. Feel free to contribute by suggesting improvements or creating pull requests. The community welcomes your input and is committed to making the tool even more powerful and user-friendly.


**In Conclusion**

With `create-aio-app`, you can accelerate your aiohttp application development by starting off with a well-structured, feature-rich project template. Whether you're a seasoned developer or just starting your Python journey, this tool provides the foundation you need to build efficient and robust web applications. Give it a try and experience the benefits firsthand!

For more information and detailed commands, check out the official [documentation](https://create-aio-app.readthedocs.io/pages/commands.html).

---



## Contributing

`create-aio-app` is a boilerplate from aiohttp community for aiohttp 
community. Feel free to make any suggestions on the issues or 
create a pull request. We will be very happy 😀. 
See [CONTRIBUTING.md](https://github.com/aio-libs/create-aio-app/blob/master/CONTRIBUTING.md) for more information about 
how to contribute to `create-aio-app`.

## License

Create aio App is an open source software <a href="https://github.com/aio-libs/create-aio-app/blob/master/LICENSE">available under the MIT license</a>.
