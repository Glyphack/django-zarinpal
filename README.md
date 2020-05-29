# django-zarinpal

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
        'zarinpal',
        ...
    )

Add django-zarinpal's URL patterns:

.. code-block:: python

    import zarrinpal


    urlpatterns = [
        ...
        path('zarinpal/', include(zarinpal_urls)),
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

        from django-zarinpal.utils import start_transaction

        data = {
            user: user object, #optional

            amount : int,

            description: str, #optional

            mobile: string, #optional

            email: string, #optional
        }
        start_transaction(data)

If you specify a callback_url in transaction data after completing transaction zarinpal will redirect user to the page you specified with two get arguments:

1.order_number: str

2.success: boolean

If you want to handle verifying transaction your self you can define your view and address it in settings with CALLBACK_URL you need to use function verify_transaction to check the transaction state it will return a transaction and you can check if it's successful or not.
you can leave it empty so package will take care of verifying transaction.

Tests
--------
Running tests: ::

    python manage.py zarinpal.tests.test_transaction
