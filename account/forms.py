from django import forms
from django.core.validators import MinValueValidator
from decimal import Decimal
from .models import Account, Transaction


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


class TransactionForm(forms.ModelForm):
    KIND_CHOICES = [
        ("0", "Despesa"),
        ("1", "Receita"),
    ]

    value_cents = forms.DecimalField(
        decimal_places=2, max_digits=10, validators=[MinValueValidator(Decimal("0.01"))]
    )
    kind = forms.ChoiceField(choices=KIND_CHOICES)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk:  # if this is an update
            self.fields["date"].disabled = True
            self.fields["value_cents"].disabled = True
            self.fields["kind"].disabled = True

    class Meta:
        model = Transaction
        fields = ["date", "value_cents", "description", "kind", "category"]
