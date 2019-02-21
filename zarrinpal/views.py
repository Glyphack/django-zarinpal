# -*- coding: utf-8 -*-
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    UpdateView,
    ListView
)

from .models import (
	Transaction,
)


class TransactionCreateView(CreateView):

    model = Transaction


class TransactionDeleteView(DeleteView):

    model = Transaction


class TransactionDetailView(DetailView):

    model = Transaction


class TransactionUpdateView(UpdateView):

    model = Transaction


class TransactionListView(ListView):

    model = Transaction

