.. Create aio app documentation master file, created by
   sphinx-quickstart on Tue Dec 25 03:13:41 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Create aio app!
==========================

What is a `create aio app`? This project is designed to quickly and simply
creating a web application based on `aiohttp` with use best practices.

A `create aio app` provide testing, documentation, deploying and a lot of
helpful boilerplate code for quickly start with `aiohttp`.


Requirements
------------

For start with `create aio app` you need to have:

   - docker
   - docker-compose


Features
--------

   - `aiohttp <https://aiohttp.readthedocs.io/en/stable/>`_ - the best python framework :)
   - `mypy <https://mypy.readthedocs.io/en/latest/>`_ - for optional static typing
   - `pytest <https://pytest.readthedocs.io/en/latest/>`_ - for run unit tests
   - `flake8 <https://flake8.readthedocs.io/en/latest/>`_ - for linting
   - `trafaret <https://trafaret.readthedocs.io/en/latest/>`_ - for validation input data
   - `aio devtools <https://github.com/aio-libs/aiohttp-devtools>`_ - helpful tool for develop
   - `aiohttp debug toolbar <https://github.com/aio-libs/aiohttp-debugtoolbar>`_ - helpful tool for debugging
   - `postgres <https://www.postgresql.org/>`_ - storage
   - `alembic <https://alembic.sqlalchemy.org/en/latest/tutorial.html>`_ - tool for create migration
   - `sqlAlchemy <https://www.sqlalchemy.org/>`_ - orm
   - `sphinx <http://www.sphinx-doc.org/en/master/>`_ - for generate docs
   - `docker-compose <https://docs.docker.com/compose/>`_ - for running develop environment and deploy

.. toctree::
   :maxdepth: 2
   :caption: Developing:

   pages/commands.rst

.. toctree::
   :maxdepth: 2
   :caption: Contents:


Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

.. This part only for the main site https://create-aio-app.readthedocs.io/
.. you can remove this block
.. meta::
   :google-site-verification: j1mO2aGrv4_nqNpK6bz7R-8cxCIvQ356YCUT8NVnbKs
   :description: The aiohttp boilerplate for quick start
   :keywords: aiohttp, boilerplate, aio, quick start
