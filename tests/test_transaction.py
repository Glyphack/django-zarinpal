from django.test import TestCase

from django_zarinpal.services import start_transaction
from .test_data import generate_test_transaction_data
from django.contrib.auth.models import User
from django_zarinpal.exceptions import AmountIsLessThanMinimum


class TestStartTransaction(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='django_zarinpal-test-user',
            email='django_zarinpal-test-user-email@example.com',
            password='YouDontKnowMe')

    def test_valid_data_start_transaction(self):
        start_transaction(generate_test_transaction_data(user=self.user))

    def test_not_valid_amount(self):
        self.assertRaises(AmountIsLessThanMinimum,
                          start_transaction,
                          generate_test_transaction_data(user=self.user,
                                                         valid_amount=False))

    def tearDown(self):
        self.user.delete()
