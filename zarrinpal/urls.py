# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.views.generic import TemplateView

from . import views


app_name = 'zarrinpal'
urlpatterns = [
    url(
        regex="^Transaction/~create/$",
        view=views.TransactionCreateView.as_view(),
        name='Transaction_create',
    ),
    url(
        regex="^Transaction/(?P<pk>\d+)/~delete/$",
        view=views.TransactionDeleteView.as_view(),
        name='Transaction_delete',
    ),
    url(
        regex="^Transaction/(?P<pk>\d+)/$",
        view=views.TransactionDetailView.as_view(),
        name='Transaction_detail',
    ),
    url(
        regex="^Transaction/(?P<pk>\d+)/~update/$",
        view=views.TransactionUpdateView.as_view(),
        name='Transaction_update',
    ),
    url(
        regex="^Transaction/$",
        view=views.TransactionListView.as_view(),
        name='Transaction_list',
    ),
	]
