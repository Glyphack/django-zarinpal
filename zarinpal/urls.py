# -*- coding: utf-8 -*-
from django.urls import path

from .views import verify_transaction_view

app_name = "zarinpal"
urlpatterns = [path("verify/", verify_transaction_view, name="verify_transaction")]
