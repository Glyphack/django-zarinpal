# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.urls import path
from django.views.generic import TemplateView

from .views import verify_transaction_view


app_name = 'zarinpal'
urlpatterns = [
        path("/verify/<str:>", verify_transaction_view, name="verify")
	]
