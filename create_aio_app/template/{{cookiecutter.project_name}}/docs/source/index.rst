.. Create aio app documentation master file, created by
   sphinx-quickstart on Tue Dec 25 03:13:41 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

The aiohttp boilerplate. A quick start for your aiohttp application.
====================================================================

What is a `create aio app`? This project is designed to quickly and simply
creating a web application based on `aiohttp` with use best practices.

A `create aio app` provide testing, documentation, deploying and a lot of
helpful boilerplate code for quickly start with `aiohttp`.

.. image:: https://raw.githubusercontent.com/aio-libs/create-aio-app/master/assets/assets.png
   :align: center


Requirements
------------

For start with `create aio app` you need to have:

   - docker
   - docker-compose


Features
--------

.. raw:: html

    <ul>
       <li>
         <a href="https://aiohttp.readthedocs.io/en/stable/" rel="nofollow">
            aiohttp
         </a>
         - the best python framework :)
       </li>
       <li>
         <a href="https://mypy.readthedocs.io/en/latest/" rel="nofollow">
            mypy
         </a>
         - for optional static typing
       </li>
       <li>
         <a href="https://pytest.readthedocs.io/en/latest/" rel="nofollow">
            pytest
         </a>
         - for run unit tests
       </li>
       <li>
         <a href="https://flake8.readthedocs.io/en/latest/" rel="nofollow">
            flake8
         </a>
         - for linting
       </li>
       <li>
         <a href="https://trafaret.readthedocs.io/en/latest/" rel="nofollow">
            trafaret
         </a>
         - for validation input data
       </li>
       <li>
         <a href="https://github.com/aio-libs/aiohttp-devtools" rel="nofollow">
            aio devtools
         </a>
         - helpful tool for develop
       </li>
       <li>
         <a href="https://github.com/aio-libs/aiohttp-debugtoolbar" rel="nofollow">
            aiohttp debugtoolbar
         </a>
         - aiohttp debug toolbar
       </li>
       <li>
         <a href="https://www.postgresql.org/" rel="nofollow">
            postgres
         </a>
         - storage
       </li>
       <li>
         <a href="https://alembic.sqlalchemy.org/en/latest/tutorial.html" rel="nofollow">
            alembic
         </a>
         - tool for create migration
       </li>
       <li>
         <a href="https://www.sqlalchemy.org/" rel="nofollow">
            sqlAlchemy
         </a>
         - orm
       </li>
       <li>
         <a href="http://www.sphinx-doc.org/en/master/" rel="nofollow">
            sphinx
         </a>
         - for generate docs
       </li>
      <li>
         <a href="https://docs.docker.com/compose/" rel="nofollow">
            docker-compose
         </a>
         - for running develop environment and deploy
       </li>
    </ul>

.. toctree::
   :maxdepth: 2
   :caption: Aiohttp Quick start:

   pages/aiohttp_quick_start.rst

.. toctree::
   :maxdepth: 2
   :caption: Developing:

   pages/commands.rst

.. toctree::
   :maxdepth: 2
   :caption: Documentation:

   pages/documentation.rst

.. toctree::
   :maxdepth: 2
   :caption: Tests:

   pages/tests.rst

.. toctree::
   :maxdepth: 2
   :caption: Contents:


Indices and tables
------------------

* :ref:`genindex`
* :ref:`search`

.. This part only for the main site https://create-aio-app.readthedocs.io/
.. you can remove this block
.. meta::
   :google-site-verification: j1mO2aGrv4_nqNpK6bz7R-8cxCIvQ356YCUT8NVnbKs
   :description: The aiohttp boilerplate for quick start your aiohttp application.
   :keywords: aiohttp, boilerplate, aio, quick start, cookiecutter, python3, pytest, sqlAlchemy, alembic
