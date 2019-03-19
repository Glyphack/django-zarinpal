# -*- coding: utf-8 -*-
from django.http import HttpResponse
from zeep import Client

from zarinpal.config import ZARINPAL_WEBSERVICE, ZARINPAL_MERCHANT_ID
from .models import (
    Transaction,
)

from .utils import verify_transaction


def verify_transaction_view(request):
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
            transaction.success(result.RefID)
            return HttpResponse('Transaction success. RefID: ' + str(result.RefID))
        elif result.Status == 101:  # todo: inspect situation
            transaction.status = result.Status
            return HttpResponse('Transaction submitted : ' + str(result.Status))
        else:  # todo: inspect situation
            transaction.status = result.Status
            return HttpResponse('Transaction failed. Status: ' + str(result.Status))
    else:
        transaction.fail('Canceled')
        return HttpResponse('Transaction failed or canceled by user')
