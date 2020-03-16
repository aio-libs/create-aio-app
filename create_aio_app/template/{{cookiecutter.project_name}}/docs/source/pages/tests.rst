Testing
=======

Code without tests is broken by design. Please remember this and write
tests;)

This project runs tests inside Docker. It allows you to run tests
locally with maximum isolation from the environment. It also
gives you a simple way of adding new resources required for your tests.

Pytest
------

Use this command to run the tests:

.. code-block:: bash

    make test

This will run flake8 and after successful execution, the command will
run a test suite with  `pytest`

If you want to run a single test, you can pass an argument
to `docker-compose` like this:

.. code-block:: bash

    docker-compose run test project_name/main/tests/test_views.py::test_view


mypy
----
Mypy is an optional static type checker for Python. We suggest you
try it out as it allows you to catch some errors, write safer
code and make refactoring of the code easier in the future.

To run mypy use this command:

.. code-block:: bash

    make mypy

Settings for mypy resides inside the mypy.ini file.

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
