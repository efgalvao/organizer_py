from django.db import models
from users.models import User, Category
from datetime import date


class Account(models.Model):
    ACCOUNT_TYPES = (
        (0, "Savings"),
        (1, "Broker"),
        (2, "Card"),
    )

    name = models.CharField(max_length=50)
    balance_cents = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    kind = models.IntegerField(choices=ACCOUNT_TYPES, default=0)

    def current_report(self):
        reference = date.today().strftime("%m%y")
        return AccountReport.objects.get(account=self, reference=reference)

    def __str__(self):
        return self.name


class AccountReport(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    date = models.DateField()
    reference = models.CharField(max_length=4)
    account_balance_cents = models.IntegerField(default=0)
    month_balance_cents = models.IntegerField(default=0)
    month_incomes_cents = models.IntegerField(default=0)
    month_expenses_cents = models.IntegerField(default=0)
    month_invested_cents = models.IntegerField(default=0)
    month_dividends_cents = models.IntegerField(default=0)

    def __str__(self):
        return self.reference

    class Meta:
        unique_together = (
            "reference",
            "account",
        )
