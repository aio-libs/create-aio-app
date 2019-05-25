Make commands
=============

The commands which exist in ``Makefile``.

Common
------


.. csv-table::
   :header: "command", "description"
   :widths: 20, 20

   ``make run (make)``, To start the project in develop mode
   ``make stop``, To stop work of docker containers
   ``make stop``, To clean up of docker containers
   ``make bash``, Interactive work inside container (the command must be running after ``make run``)
   ``make upgrade``, To upgrade dependencies



Testing
-------



.. csv-table::
   :header: "command", "description"
   :widths: 20, 20

   ``make test``, To start the ``pytest`` with docker
   ``make mypy``, To run ``mypy`` for type checking
   ``make black``, To run ``black`` for formatting code
   ``make lint``, To run flake8 (The all settings connected with a ``flake8`` you can customize in ``.flake8``)



Database
--------
If u have ``postgres``


.. csv-table::
   :header: "command", "description"
   :widths: 20, 20

   ``make migrations``, To generate a new migration
   ``make migrate``, To apply migrations
   ``make psql``, To connect to postgres


Other
-----

.. csv-table::
   :header: "command", "description"
   :widths: 20, 20

   ``make doc``, To generate a sphinx documentation

