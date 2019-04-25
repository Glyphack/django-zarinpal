from zeep import Client
import logging

from zarinpal.helpers import generate_start_transaction_data
from .config import (
    ZARINPAL_START_GATEWAY,
    ZARINPAL_WEBSERVICE,
)
from .models import Transaction


def start_transaction(transaction_data: dict) -> str:
    transaction = Transaction.objects.create_transaction(transaction_data)
    start_transaction_data = generate_start_transaction_data(transaction)
    client = Client(ZARINPAL_WEBSERVICE)
    result = client.service.PaymentRequest(
        start_transaction_data["merchant_id"],
        start_transaction_data["amount"],
        start_transaction_data["description"],
        start_transaction_data["email"],
        start_transaction_data["mobile"],
        start_transaction_data["callback_url"],
    )
    print(start_transaction_data)
    if result.Status == 100:
        transaction.authority = result.Authority
        transaction.save(update_fields=["authority"])
        return ZARINPAL_START_GATEWAY + result.Authority
    else:
        logging.error(result)
