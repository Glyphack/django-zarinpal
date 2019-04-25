# -*- coding: utf-8 -*-
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.utils import timezone
from hashid_field import HashidField
from django.conf import settings

from .exceptions import CallbackUrlNotProvided
from .config import TRANSACTION_STATUS_CHOICES, ZARINPAL_START_GATEWAY
from .managers import TransactionManager


class Transaction(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True)
    amount = models.DecimalField(
        max_digits=64, decimal_places=2, default=0, blank=True, null=True
    )
    authority = models.CharField(max_length=100, blank=True, null=True)
    ref_id = models.IntegerField(null=True, blank=True)
    description = models.TextField()
    callback_url = models.CharField(max_length=100)
    first_name = models.CharField(max_length=225, blank=True, null=True)
    last_name = models.CharField(max_length=225, blank=True, null=True)
    email = models.CharField(max_length=225, blank=True, null=True)
    mobile = models.CharField(max_length=225, blank=True, null=True)
    order_number = HashidField(
        allow_int_lookup=True, blank=True, null=True, salt=getattr(settings, "secret_key", None)
    )
    address = models.CharField(max_length=225, blank=True, null=True)
    country = models.CharField(max_length=225, blank=True, null=True)
    postal_code = models.CharField(max_length=225, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    successful_payment_date_time = models.DateTimeField(blank=True, null=True)
    # status = models.CharField(max_length=100, choices=TRANSACTION_STATUS_CHOICES)
    status = models.CharField(max_length=100)
    failure_reason = models.CharField(max_length=100, blank=True, null=True)
    simulation = models.BooleanField(default=False)
    objects = TransactionManager()

    def __repr__(self):
        return "<zarinpal id:{0}>".format(self.order_number)

    def __str__(self):
        return "zarinpal: {0}".format(self.order_number)

    def success(self, ref_id):
        self.ref_id = ref_id
        self.status = "SUCCESS"
        self.successful_payment_date_time = timezone.now()
        self.save(update_fields=["status", "successful_payment_date_time", "ref_id"])

    def fail(self, failure_reason=None):
        self.status = "FAILED"
        if failure_reason:
            self.failure_reason = failure_reason
        self.save(update_fields=["status", "failure_reason"])

    def is_successful(self):
        return self.status == "SUCCESS"

    def get_transaction_start_url(self, request=None):
        if self.simulation is False:
            return ZARINPAL_START_GATEWAY + self.authority
        else:
            relative_start_url = reverse(
                "zarinpal:sandbox-payment", kwargs={"authority_start": self.authority}
            )
            if request:
                return request.build_absolute_uri(relative_start_url)
            else:
                return relative_start_url

    def get_client_callback_url(self):
        if self.callback_url:
            return self.callback_url + f"?orderNumber={self.order_number}"
        else:
            raise CallbackUrlNotProvided(
                f"Callback url is not set in transaction with order number {self.order_number.hashid}"
            )
