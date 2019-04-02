from django.dispatch import Signal

transaction_verified = Signal(providing_args=["transaction"])
