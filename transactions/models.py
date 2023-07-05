from django.db import models
from django.conf import settings
from customers_app.models import Account
import uuid


class Transactions(models.Model):
    transferer = models.ForeignKey(Account, on_delete=models.CASCADE, null=False)
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, unique=True)
    transferer_name = models.CharField(max_length=200, null=False)
    receiver = models.CharField(max_length=250, null=False, blank=False)
    receiver_acct = models.CharField(max_length=12, null=False)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    remark = models.CharField(max_length=100, null=True)
    alert_type = models.CharField(max_length=50, null=False)
    time_processed = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.receiver
