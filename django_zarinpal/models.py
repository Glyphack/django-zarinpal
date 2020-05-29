from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.utils import timezone
from hashid_field import HashidAutoField

from django_zarinpal.config import ZARINPAL_START_GATEWAY


class Transaction(models.Model):
    order_number = HashidAutoField(
        primary_key=True,
        allow_int_lookup=True,
        salt=getattr(settings, "HASHID_FIELD_SALT", None)
    )
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=64, decimal_places=2)
    authority = models.CharField(max_length=100, blank=True, null=True)
    ref_id = models.IntegerField(null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    verified_at = models.DateTimeField(blank=True, null=True)

    TRANSACTION_STATUS_CHOICES = (
        ("PENDING", "Transaction has just started"),
        ("FAILED", "Transaction has failed"),
        ("SUCCESS", "Transaction has successfully done"),
    )
    status = models.CharField(
        max_length=100,
        choices=TRANSACTION_STATUS_CHOICES,
        default="PENDING"
    )
    failure_reason = models.CharField(max_length=100, blank=True, null=True)
    is_test = models.BooleanField(default=False)

    def success(self, ref_id):
        self.ref_id = ref_id
        self.status = "SUCCESS"
        self.verified_at = timezone.now()
        self.save(
            update_fields=["status", "verified_at", "ref_id"]
        )

    def fail(self, failure_reason=""):
        self.status = "FAILED"
        if failure_reason:
            self.failure_reason = failure_reason
            self.save(update_fields=["status", "failure_reason"])
        else:
            self.save(update_fields=["status"])

    def is_successful(self):
        return self.status == "SUCCESS"

    def get_transaction_start_url(self, request=None):
        if self.is_test is False:
            return ZARINPAL_START_GATEWAY + self.authority
        else:
            relative_start_url = reverse(
                "django_zarinpal:sandbox-payment",
                kwargs={"authority_start": self.authority}
            )
            if request:
                return request.build_absolute_uri(relative_start_url)
            else:
                return relative_start_url
