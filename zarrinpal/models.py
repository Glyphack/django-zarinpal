# -*- coding: utf-8 -*-
from django.contrib.auth import get_user_model
from django.db import models
from hashid_field import HashidField

from .config import TRANSACTION_STATUS_CHOICES
from .managers import TransactionManager


class Transaction(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True)
    amount = models.DecimalField(max_digits=64, decimal_places=2, default=0, blank=True, null=True)
    authority_start = models.CharField(max_length=100, blank=True, null=True)  # by module
    authority_verify = models.CharField(max_length=100, blank=True, null=True)  # by module
    description = models.TextField()
    callback_url = models.CharField(max_length=100)
    first_name = models.CharField(max_length=225)
    last_name = models.CharField(max_length=225)
    email = models.CharField(max_length=225)
    mobile = models.CharField(max_length=225)
    order_number = HashidField(
        allow_int_lookup=True,
        blank=True,
        null=True
    )
    address = models.CharField(max_length=225)
    country = models.CharField(max_length=225)
    postal_code = models.CharField(max_length=225)
    city = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)  # by module
    successful_payment_date_time = models.DateTimeField(blank=True, null=True)  # by module
    status = models.CharField(max_length=100, choices=TRANSACTION_STATUS_CHOICES)  # by module
    failure_reason = models.CharField(max_length=100, blank=True, null=True)  # by module
    simulation = models.BooleanField(default=False)
    objects = TransactionManager()

class Transaction(TimeStampedModel):
    pass
    


