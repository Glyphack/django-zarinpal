class ZarinpalException(Exception):
    """
    BaseClass for exceptions
    """


class TransactionDoesNotExist(ZarinpalException):
    """ No transaction submitted with this authority """


class TransactionDataIsNotValid(ZarinpalException):
    """ The data was not valid for Zarinpal gateway"""


class CouldNotStartTransaction(ZarinpalException):
    """did not get start authority from Zarinpal"""


class AmountIsLessThanMinimum(ZarinpalException):
    """minimum amount to start transaction is 1000"""


class CallBackUrlNotSet(ZarinpalException):
    """Specify ZARINPAL_CALLBACK_URL in settings"""


class MerchantIdNotSet(ZarinpalException):
    """Specify ZARINPAL_MERCHANT_ID in settings"""