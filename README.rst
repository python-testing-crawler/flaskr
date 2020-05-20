Flaskr *with a crawler*
=======================

The basic blog app built in the Flask `tutorial`_.

.. _tutorial: https://flask.palletsprojects.com/tutorial/

Extracted from https://github.com/pallets/flask

Added:

* Test dependency on `python-testing-crawler`
* `tests/test_crawl.py`


Test
----

To run all the tests, including the crawler tests, create a new virtualenv,
activate it and then:

::

    $ pip install '.[test]'
    $ pytest

Run with coverage report::

    $ coverage run -m pytest
    $ coverage report
    $ coverage html  # open htmlcov/index.html in a browser
