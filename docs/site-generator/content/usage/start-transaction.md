---
title= "Start Transaction"
date= 2019-03-27T12:40:06+04:30
draft= true
weight = 1
---

## how to start a transaction
<!--more-->

you need to use function start_transaction with a dictionary containing your transaction data like this: .. code-block:: python

    data = {

        user: user object, #optional

        first_name: str, #optional

        last_name: str, #optional

        amount : int,

        callback_url, #optional

        description: str, #optional

        mobile: string, #optional

        email: string, #optional

    }
    start_transaction(transaction_data)

this function will return a url you need to redirect user to after completing transaction user will be redirected to the url you specified in transaction_data with get parameter order_number and success.

## verification proccess
after completing transaction zarinpal will rederict user to www.yoursite.com/zarinpal/verify this view will verify user transaction and update the transaction objecct associated with that payment.
there is also a verify_transaction signal that will send transaction object after verification.
the view will redirect user to the callback_url you specified in transaction data.

If you specify a callback_url in settings after completing transaction zarinpal will redirect user to the page you specified with two get arguments:

1.order_number

2.success: boolean

If you want to handle verifying transaction your self you can define your view and address it in settings with CALLBACK_URL you need to use function verify_transaction to check the transaction state it will return a transaction and you can check if it's successful or not. you can leave it empty so package will take care of verifying transaction.