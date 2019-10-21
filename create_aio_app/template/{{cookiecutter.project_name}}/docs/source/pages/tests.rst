Testing
=======

The code without any tests is a code that will be rewritten. Pleace remember
this and write tests ;)

For running tests we use docker. It's the best way for running your tests
locally with maximum isolation from environment. Also docker give simple way
for add test resources in one line.

Pytest
------

For running tests you should use this command:

.. code-block:: bash

    make test

This command running flake8 and after success run test by `pytest`

If you want to run a single test, you can pass an argument
to `docker-compose` like this:

.. code-block:: bash

    docker-compose run test project_name/main/tests/test_views.py::test_view


mypy
----
Mypy is static type checker for Python. We recommend used mypy because this
type checker make your code more safe and make refactoring easier.

For running mypy you should use this command:

.. code-block:: bash

    make mypy

All settings for mypy are in the mypy.ini file.

Read more:
----------

.. raw:: html

    <ul>
       <li>
         <a href="https://docs.pytest.org/en/latest/contents.html" rel="nofollow">
            pytest
         </a>
         - the official documentation for pytest
       </li>
       <li>
         <a href="https://mypy.readthedocs.io/en/latest/" rel="nofollow">
            mypy
         </a>
         - the official documentation for mypy
       </li>
    </ul>
