# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import redirect
from zeep import Client

from zarinpal.config import ZARINPAL_WEBSERVICE, ZARINPAL_MERCHANT_ID
from .models import Transaction

from zarinpal.helpers import verify_transaction
from .signals import transaction_verified


def verify_transaction_view(request):
    authority = request.GET.get("Authority")
    status = request.GET.get("Status")
    transaction = verify_transaction(status, authority)
    transaction_verified.send(sender=None, transaction=transaction)
    print("verified")
    if transaction.callback_url:
        return redirect(
            transaction.callback_url
            + f"/?success={transaction.is_successful()}&orderNumber={transaction.order_number}"
        )
    return HttpResponse(f"done transaction{authority}")
    # return redirect(
    #    transaction.callback_url
    # )
