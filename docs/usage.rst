=====
Usage
=====

To use django-zarrinpal in a project, add it to your `INSTALLED_APPS`:

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
