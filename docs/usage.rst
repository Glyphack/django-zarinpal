=====
Usage
=====

To use django-zarinpal in a project, add it to your `INSTALLED_APPS`:

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
