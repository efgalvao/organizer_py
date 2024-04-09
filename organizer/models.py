from django.db import models
from users.models import User


class Account(models.Model):
    name = models.CharField(max_length=100)
    balance_cents = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    kind = models.IntegerField(null=False, default=0)

    def __str__(self):
        return self.name
