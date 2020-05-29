from django.urls import path

from django_zarinpal.views import verify_transaction_view

app_name = "django_zarinpal"
urlpatterns = [
    path(
        "verify/", verify_transaction_view, name="default_verify_transaction"
    )
]
