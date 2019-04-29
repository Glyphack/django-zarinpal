def generate_test_transaction_data(user, valid_amount=True):
    if valid_amount:
        amount = 2000
    else:
        amount = 1
    return {"user": user,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "amount": amount,
            "callback_url": None,
            "description": "charge account",
            "email": user.email,
            "mobile": "",
            }
