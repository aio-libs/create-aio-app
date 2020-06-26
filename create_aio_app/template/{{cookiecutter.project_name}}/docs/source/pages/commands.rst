Make commands
=============

The set of commands available in the ``Makefile``.

Common
------


.. csv-table::
   :header: "command", "description"
   :widths: 20, 20

   ``make run (make)``, Start the development server
   ``make stop``, Stop docker containers
   ``make clean``, Clean up of docker containers
   ``make bash``, Interactive shell inside the running container (the command can be executed only if the server is running e.g. after ``make run``)
   ``make upgrade``, Upgrade dependencies



Testing
-------



.. csv-table::
   :header: "command", "description"
   :widths: 20, 20

   ``make test``, Run the ``pytest`` suite inside docker
   ``make mypy``, Run ``mypy`` for type checking
   ``make black``, Run ``black`` code formatter
   ``make lint``, Run flake8 (All the settings for `flake8` can be customized in `.flake8` file)
   ``make profile``, Run ``py-spy`` sampling profiler. It defaults to 60 seconds. Can be change by adding the ``TIME`` variable. eg ``make profile TIME=30``



Database
--------
Next commands are available if you have not disabled ``postgres`` option when
creating a project:


.. csv-table::
   :header: "command", "description"
   :widths: 20, 20

   ``make migrations``, Generate a new migration
   ``make migrate``, Apply migrations
   ``make psql``, Connect to the postgres inside running container


Other
-----

.. csv-table::
   :header: "command", "description"
   :widths: 20, 20

   ``make doc``, Generate a sphinx documentation

