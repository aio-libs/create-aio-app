Documentation
=============

The best thing that you can do for yourself in future it's written test and
documentation about your web service. Here we will talk about how organization
documentation in your project.

Structure
---------

For this boilerplate we use this structure:

   - **pages/** -
     the directory for all `*.rst` files connected with boilerplate
   - **project/** -
     the directory should include `*.rst` files which include info
     about your project (auto generated docs, business logic etc.)

All new files you should add to *index.rst*.

Linter
------

`Doc8 <https://github.com/openstack/doc8>`_ is an opinionated style checker
for *rst* styles of documentation. We use this linter as the default in this
boilerplate.

Read more:
----------

    - `Sphinx <http://www.sphinx-doc.org/en/master/usage/quickstart.html>`_ - the official documentation for sphinx

    - `Documentation style guide <https://documentation-style-guide-sphinx.readthedocs.io/en/latest/style-guide.html>`_ - the recommended style guide
