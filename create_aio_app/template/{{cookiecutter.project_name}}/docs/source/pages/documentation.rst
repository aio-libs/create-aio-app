Documentation
=============

The best thing you can do for future self and fellow contributors is to write
both tests and documentation about your project. This section explains how to
structure and organize documentation in your project.

Structure
---------

We use the following structure:

   - **pages/** -
     The directory for all `*.rst` files about the boilerplate.
   - **project/** -
     This directory is for `*.rst` files associated with your project
     (this can include auto-generated docs, business logic, etc.)

All new files should be added to *index.rst*.

Linter
------

`Doc8 <https://github.com/openstack/doc8>`_ is an opinionated style checker
for *rst* styles of documentation. This linter used by default.

Read more:
----------

.. raw:: html

    <ul>
       <li>
         <a href="http://www.sphinx-doc.org/en/master/usage/quickstart.html" rel="nofollow">
            Sphinx
         </a>
         - official sphinx documentation
       </li>
       <li>
         <a hef="https://documentation-style-guide-sphinx.readthedocs.io/en/latest/style-guide.html" rel="nofollow">
            Documentation style guide
         </a>
        - recommended style guide
       </li>
       <li>
         <a href="https://github.com/openstack/doc8" rel="nofollow">
            Doc8
         </a>
        - style checker for documentation
       </li>
    </ul>
