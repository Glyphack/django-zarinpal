#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_django-zarinpal
------------

Tests for `django-zarinpal` models module.
"""

from django.test import TestCase

from zarinpal.models import Transaction
from .test_data import valid_transaction_data
from zarinpal.utils import start_transaction


class TestZarinpal(TestCase):
    def setUp(self):
        pass

    def test_creating_simulation_transaction(self):
        start_transaction(**valid_transaction_data)

    def tearDown(self):
        pass
