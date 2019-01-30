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

`Doc8` is an opinionated style checker
for *rst* styles of documentation. We use this linter as the default in this
boilerplate.

Read more:
----------

.. raw:: html

    <ul>
       <li>
         <a href="http://www.sphinx-doc.org/en/master/usage/quickstart.html" rel="nofollow">
            Sphinx
         </a>
         - the official documentation for sphinx
       </li>
       <li>
         <a href="https://documentation-style-guide-sphinx.readthedocs.io/en/latest/style-guide.html" rel="nofollow">
            Documentation style guide
         </a>
        - the recommended style guide
       </li>
       <li>
         <a href="https://github.com/openstack/doc8" rel="nofollow">
            Doc8
         </a>
        - style checker for documentation
       </li>
    </ul>
