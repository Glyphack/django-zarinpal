from django.contrib.sites.models import Site
from django.http import HttpResponse
from django.urls import reverse
from zeep import Client

from zarinpal.helpers import generate_start_transaction_data
from .config import (
    ZARINPAL_MERCHANT_ID,
    ZARINPAL_SIMULATION,
    ZARINPAL_START_GATEWAY,
    ZARINPAL_WEBSERVICE,
    ZARINPAL_CALLBACK_URL)
from .models import Transaction


def start_transaction(transaction_data: dict, simulation: bool = ZARINPAL_SIMULATION) -> str:
    transaction = Transaction.objects.create_transaction(transaction_data)
    start_transaction_data = generate_start_transaction_data(transaction)
    client = Client(ZARINPAL_WEBSERVICE)
    result = client.service.PaymentRequest(
        start_transaction_data['merchant_id'],
        start_transaction_data['amount'],
        start_transaction_data['description'],
        start_transaction_data['email'],
        start_transaction_data['mobile'],
        start_transaction_data['callback_url'],
    )
    if result.Status == 100:
        return ZARINPAL_START_GATEWAY + result.Authority


def verify_transaction(request) -> HttpResponse:
    client = Client(ZARINPAL_WEBSERVICE)
    authority = request.GET['Authority']
    transaction = Transaction.objects.get(authority=authority)
    if not transaction:
        return HttpResponse('this request does not have a started transaction')
    if request.GET.get("Status") == "OK":
        result = client.service.PaymentVerification(
            ZARINPAL_MERCHANT_ID, authority, transaction.amount
        )
        if result.Status == 100:
            transaction.success()
            transaction.ref_id = result.RefID
            return HttpResponse('Transaction success. RefID: ' + str(result.RefID))
        elif result.Status == 101:
            transaction.status = result.Status
            return HttpResponse('Transaction submitted : ' + str(result.Status))
        else:
            transaction.status = result.Status
            return HttpResponse('Transaction failed. Status: ' + str(result.Status))
    else:
        transaction.fail('Canceled')
        return HttpResponse('Transaction failed or canceled by user')


def get_call_back_url():
    if ZARINPAL_CALLBACK_URL:
        return ZARINPAL_CALLBACK_URL
    else:
        return Site.objects.get_current().domain + reverse(
            'zarinpal:verify_transaction',
        )
