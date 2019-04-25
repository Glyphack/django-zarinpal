from zarinpal.config import ZARINPAL_WEBSERVICE, ZARINPAL_MERCHANT_ID, ZARINPAL_CALLBACK_URL
from zarinpal.exceptions import TransactionDoesNotExist
from zarinpal.models import Transaction
from zeep import Client


def verify_transaction(status: str, authority: int) -> Transaction:
    client = Client(ZARINPAL_WEBSERVICE)
    try:
        transaction = Transaction.objects.get(status="PENDING", authority=authority)
    except Transaction.DoesNotExist:
        raise TransactionDoesNotExist
    if status == "OK":
        result = client.service.PaymentVerification(
            ZARINPAL_MERCHANT_ID, authority, transaction.amount
        )
        if result.Status == 100:
            transaction.success(result.RefID)
        elif result.Status == 101:
            transaction.status = result.Status
            return HttpResponse("Transaction submitted : " + str(result.Status))
        else:
            transaction.fail(result.Status)
    else:
        transaction.fail("Canceled")

    return transaction


def generate_start_transaction_data(transaction):
    return {
        "merchant_id": ZARINPAL_MERCHANT_ID,
        "amount": transaction.amount,
        "description": transaction.description,
        "email": transaction.email,
        "mobile": transaction.mobile,
        "callback_url": get_callback_url(),
    }


def get_callback_url():
    if ZARINPAL_CALLBACK_URL:
        return ZARINPAL_CALLBACK_URL
    else:
        return (
            "http://"
            + Site.objects.get_current().domain
            + reverse("zarinpal:verify_transaction")
        )
