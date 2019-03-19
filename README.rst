=============================
django-zarinpal
=============================

.. image:: https://badge.fury.io/py/django-zarinpal.svg
    :target: https://badge.fury.io/py/django-zarinpal

.. image:: https://travis-ci.org/glyphack/django-zarinpal.svg?branch=master
    :target: https://travis-ci.org/glyphack/django-zarinpal

.. image:: https://codecov.io/gh/glyphack/django-zarinpal/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/glyphack/django-zarinpal

django package for integrating payments with zarinpal

Documentation
-------------

The full documentation is at https://django-zarinpal.readthedocs.io.

Quickstart
----------

Install django-zarinpal::

    pip install django-zarinpal

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'zarinpal.apps.ZarinpalConfig',
        ...
    )

Add django-zarinpal's URL patterns:

.. code-block:: python

    from zarinpal import urls as zarinpal_urls


    urlpatterns = [
        ...
        url(r'^', include(zarinpal_urls)),
        ...
    ]

Features
--------

* TODO

How to Use
----------
set these variables in your settings file:
1.ZARINPAL_CALLBACK_URL
2.ZARINPAL_SIMULATION
3.ZARINPAL_MERCHANT_ID (you may leave it blank if you set the simulation to True

you have to use function start_transaction with a dictionary containing your transaction data like this:
.. code-block:: python

        data = {
            amount : int,
            description: str, #optional
            mobile: string, #optional
            email: string, #optional
        }

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
