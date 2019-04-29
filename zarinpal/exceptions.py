class ZarinpalError(Exception):
    """
    BaseClass for exceptions
    """


class UnknownTransactionFailure(ZarinpalError):
    """ Unknown transaction failure """


class UnknownTransactionStatusCode(ZarinpalError):
    """ Unknown transaction status code """


class CallbackUrlNotProvided(ZarinpalError):
    """ callback url is not provided in transaction data or project settings """


class TransactionDoesNotExist(ZarinpalError):
    """ No transaction submitted with this authority """


class TransactionDataIsNotValid(ZarinpalError):
    """ The data was not valid for Zarinpal gateway"""


class CouldNotStartTransaction(ZarinpalError):
    """did not get start authority from Zarinpal"""


class AmountIsLessThanMinimum(ZarinpalError):
    """minimum amount to start transaction is 1000"""
