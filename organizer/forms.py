from django import forms
from django.core.validators import MinValueValidator
from decimal import Decimal
from .models import Account


class AccountForm(forms.ModelForm):
    KIND_CHOICES = [
        ("1", "Banco"),
        ("2", "Corretora"),
        ("3", "Cartão"),
    ]

    balance_cents = forms.DecimalField(
        decimal_places=2, max_digits=10, validators=[MinValueValidator(Decimal("0.01"))]
    )
    kind = forms.ChoiceField(choices=KIND_CHOICES)

    class Meta:
        model = Account
        fields = ["name", "balance_cents", "kind"]
