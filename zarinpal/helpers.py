from .config import ZARINPAL_MERCHANT_ID
from .utils import get_call_back_url


def generate_start_transaction_data(transaction):
    return {
        'merchant_id': ZARINPAL_MERCHANT_ID,
        "amount": transaction.amount,
        "description": transaction.description,
        "email": transaction.email,
        "mobile": transaction.mobile,
        "callback_url": get_call_back_url(),
    }
