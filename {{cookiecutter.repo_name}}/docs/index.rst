{{cookiecutter.repo_name|capitalize}} Documentation
==========================

----

Getting Started
---------------

Core concepts and calls explanations

.. toctree::
    :maxdepth: 2

    changelog

Concepts
--------

.. toctree::
    :maxdepth: 2
    :glob:

    concepts/*

User Guide
----------

.. toctree::
    :maxdepth: 2
    :glob:

    guide/*

API Reference
-------------

Auto-generated API documentation

.. toctree::
    :maxdepth: 1
    :glob:

    {{cookiecutter.repo_name}}/api
    {{cookiecutter.repo_name}}/api/*
    {{cookiecutter.repo_name}}/services/*
    {{cookiecutter.repo_name}}/*

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
