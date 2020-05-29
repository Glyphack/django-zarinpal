# django-zarinpal

Integrate django payments with [zarinpal](https://www.zarinpal.com)


Features
--------

- sending signal on verifying transaction to let other apps know about it

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



### How to Use

set these variables in your settings file:

```python

ZARINPAL_CALLBACK_URL: bool # the url user redirects to after transaction

ZARINPAL_SIMULATION: bool # is transactions for test?

ZARINPAL_MERCHANT_ID: str # merchant id from zarinpal (you may leave it blank if you set the simulation to True)
```

you can use function `start_transaction` with a dictionary containing your transaction data like this:

```python
from django.shortcuts import redirect
from django_zarinpal.services import start_transaction


def start_payment(request):
    result = start_transaction(
        {
            "user": request.user,
            "amount": 10000,
            "description": "transaction description",
            "mobile": "09123456789",
            "email": "string",
        }
    )
    return redirect(result) # result is the url for starting transaction
```

If you specify a callback_url in transaction data after completing transaction zarinpal will redirect user to the page you specified with two get arguments:

1.order_number: str

2.success: boolean

### Custom verification

If you want to handle verifying transaction your self you can define your view and 
address it in settings with ZARINPAL_VERIFY_TRANSACTION_VIEW. you can use function
`verify_transaction` to verify a transaction.

If you don't specify this view, package will use default view for verifying transactions.

Tests
--------
Running tests: ::

    python manage.py runtests.py
