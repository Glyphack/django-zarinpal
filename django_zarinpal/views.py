from django.http import HttpResponseRedirect

from django_zarinpal.config import ZARINPAL_CALLBACK_URL
from django_zarinpal.services import (
    verify_transaction
)
from django_zarinpal.signals import transaction_verified


def verify_transaction_view(request):
    authority = request.GET.get("Authority")
    status = request.GET.get("Status")
    transaction = verify_transaction(status, authority)
    transaction_verified.send(sender=None, transaction=transaction)
    return HttpResponseRedirect(
        ZARINPAL_CALLBACK_URL +
        f"?success={transaction.is_successful()}"
        f"?order_number={transaction.order_number}"
    )
