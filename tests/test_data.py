def generate_test_transaction_data(user, valid_amount=True):
    if valid_amount:
        amount = 2000
    else:
        amount = 1
    return {
        "user": user,
        "amount": amount,
        "description": "charge account",
        "email": user.email,
        "mobile": "0234934",
    }
