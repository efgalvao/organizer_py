from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"


class Financing(models.Model):
    name = models.CharField(max_length=100)
    borrowed_value_cents = models.IntegerField()
    parcels = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Financings"


class Installment(models.Model):
    financing = models.ForeignKey(
        Financing, related_name="installments", on_delete=models.CASCADE
    )
    ordinary = models.BooleanField(default=True)
    parcel = models.IntegerField()
    paid_parcels = models.IntegerField()
    payment_date = models.DateField()
    amortization_cents = models.IntegerField()
    interest_cents = models.IntegerField()
    insurance_cents = models.IntegerField()
    fees_cents = models.IntegerField()
    monetary_correction_cents = models.IntegerField()
    adjustment_cents = models.IntegerField()

    def __str__(self):
        return f"{self.financing.name} - {self.parcel}"

    class Meta:
        verbose_name_plural = "Installments"


class Transference(models.Model):
    receiver = models.ForeignKey(
        "account.Account", related_name="receiver", on_delete=models.CASCADE
    )
    sender = models.ForeignKey(
        "account.Account", related_name="sender", on_delete=models.CASCADE
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    value_cents = models.IntegerField()
    date = models.DateField()
