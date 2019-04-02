from django.conf import settings

ZARINPAL_WEBSERVICE = "https://www.zarinpal.com/pg/services/WebGate/wsdl"
ZARINPAL_START_GATEWAY = "https://www.zarinpal.com/pg/StartPay/"
ZARINPAL_CALLBACK_URL = getattr(settings, "ZARINPAL_CALLBACK_URL", None)
ZARINPAL_SIMULATION = getattr(settings, "ZARINPAL_SIMULATION", False)
ZARINPAL_MERCHANT_ID = getattr(settings, "ZARINPAL_MERCHANT_ID", "")

if ZARINPAL_SIMULATION:
    ZARINPAL_WEBSERVICE = "https://sandbox.zarinpal.com/pg/services/WebGate/wsdl"
    ZARINPAL_START_GATEWAY = "https://sandbox.zarinpal.com/pg/StartPay/"
    ZARINPAL_MERCHANT_ID = "XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX"

TRANSACTION_STATUS_CHOICES = [
    ("PENDING", "Transaction has just started"),
    ("INCOMPLETE_PARAMETERS", "Transaction parameters were incomplete"),
    ("MERCHANT_CODE_INCORRECT", "Merchant code was incorrect"),
    ("MERCHANT_CODE_NOT_ACTIVE", "Merchant code is not active"),
    ("AUTHORITY_CODE_INVALID", "Authority code was invalid"),
    ("ALREADY_VERIFIED", "Transaction was already verified"),
    ("FAILED", "Transaction was failed"),
    ("UNKNOWN", "Transaction was failed with unknown error"),
    ("SUCCESS", "Transaction was successfully done"),
]
TRANSACTION_STATUS_CODES = {
    -1: "INCOMPLETE_PARAMETERS",
    -2: "MERCHANT_CODE_INCORRECT",
    -3: "MERCHANT_CODE_NOT_ACTIVE",
    -8: "AUTHORITY_CODE_INVALID",
    -9: "ALREADY_VERIFIED",
    -10: "FAILED",
    -100: "UNKNOWN",
    100: "SUCCESS",
}
