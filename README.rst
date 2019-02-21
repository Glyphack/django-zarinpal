=============================
django-zarrinpal
=============================

.. image:: https://badge.fury.io/py/django-zarrinpal.svg
    :target: https://badge.fury.io/py/django-zarrinpal

.. image:: https://travis-ci.org/glyphack/django-zarrinpal.svg?branch=master
    :target: https://travis-ci.org/glyphack/django-zarrinpal

.. image:: https://codecov.io/gh/glyphack/django-zarrinpal/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/glyphack/django-zarrinpal

django package for integrating payments with zarrinpal

Documentation
-------------

The full documentation is at https://django-zarrinpal.readthedocs.io.

Quickstart
----------

Install django-zarrinpal::

    pip install django-zarrinpal

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'zarrinpal.apps.ZarrinpalConfig',
        ...
    )

Add django-zarrinpal's URL patterns:

.. code-block:: python

    from zarrinpal import urls as zarrinpal_urls


    urlpatterns = [
        ...
        url(r'^', include(zarrinpal_urls)),
        ...
    ]

Features
--------

* TODO

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox

Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
