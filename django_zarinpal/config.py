from django.conf import settings

from django_zarinpal.exceptions import CallBackUrlNotSet, MerchantIdNotSet

ZARINPAL_WEBSERVICE = "https://www.zarinpal.com/pg/services/WebGate/wsdl"
ZARINPAL_START_GATEWAY = "https://www.zarinpal.com/pg/StartPay/"
ZARINPAL_VERIFY_TRANSACTION_VIEW = getattr(
    settings,
    "ZARINPAL_VERIFY_TRANSACTION_VIEW",
    "django_zarinpal:default_verify_transaction"
)
ZARINPAL_SANDBOX = getattr(settings, "ZARINPAL_SIMULATION", False)

ZARINPAL_CALLBACK_URL = getattr(settings, "ZARINPAL_CALLBACK_URL", None)
if not ZARINPAL_CALLBACK_URL:
    raise CallBackUrlNotSet("Specify ZARINPAL_CALLBACK_URL in settings")

ZARINPAL_MERCHANT_ID = getattr(settings, "ZARINPAL_MERCHANT_ID", None)
if not ZARINPAL_SANDBOX and not ZARINPAL_MERCHANT_ID:
    raise MerchantIdNotSet("Specify ZARINPAL_MERCHANT_ID in settings")

if ZARINPAL_SANDBOX:
    ZARINPAL_WEBSERVICE = "https://sandbox.zarinpal.com/pg/services/WebGate/wsdl"
    ZARINPAL_START_GATEWAY = "https://sandbox.zarinpal.com/pg/StartPay/"
    ZARINPAL_MERCHANT_ID = "XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX"
