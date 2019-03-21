class Error(Exception):
    """
    BaseClass for exceptions
    """


class UnknownTransactionFailure(Error):
    """ Unknown transaction failure """


class UnknownTransactionStatusCode(Error):
    """ Unknown transaction status code """


class CallbackUrlNotProvided(Error):
    """ callback url is not provided in transaction data or project settings """


class TransactionDoesNotExist(Error):
    """ No transaction submitted with this authority """
