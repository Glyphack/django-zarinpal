from django.test import TestCase

from zarinpal.utils import start_transaction
from .test_data import valid_transaction_data


class TestStartTransaction(TestCase):
    def setUp(self):
        pass

    def test_valid_data_transaction(self):
        start_transaction(**valid_transaction_data)

    def tearDown(self):
        pass
