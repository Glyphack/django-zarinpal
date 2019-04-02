from django.db.models import manager

from .config import ZARINPAL_SIMULATION


class TransactionManager(manager.Manager):
    """ Manager for :class:`Transaction` """

    def create_transaction(self, transaction_data):
        transaction_data["status"] = "PENDING"
        transaction_data["simulation"] = ZARINPAL_SIMULATION
        created_transaction = self.create(**transaction_data)
        created_transaction.order_number = created_transaction.id
        created_transaction.save(update_fields=["order_number"])
        return created_transaction
