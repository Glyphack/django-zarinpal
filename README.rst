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

The full documentation is at https://glyphack.github.io/django-zarinpal/.

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

- sending signal on verifying transaction to let other apps know about it

How to Use
----------
set these variables in your settings file:
1.ZARINPAL_CALLBACK_URL(if you want to handle verification yourself explained here)

2.ZARINPAL_SIMULATION

3.ZARINPAL_MERCHANT_ID (you may leave it blank if you set the simulation to True


you have to use function start_transaction with a dictionary containing your transaction data like this:
.. code-block:: python

        from django-zarinpal import start_transaction

        data = {
            user: user object, #optional

            first_name: str, #optional

            last_name: str, #optional

            amount : int,

            callback_url, #optional

            description: str, #optional

            mobile: string, #optional

            email: string, #optional


        }

        start_transaction(data)

If you specify a callback_url in transaction data after completing transaction zarinpal will redirect user to the page you specified with two get arguments:

1.order_number

2.success: boolean

If you want to handle verifying transaction your self you can define your view and address it in settings with CALLBACK_URL you need to use function verify_transaction to check the transaction state it will return a transaction and you can check if it's successful or not.
you can leave it empty so package will take care of verifying transaction.

Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
