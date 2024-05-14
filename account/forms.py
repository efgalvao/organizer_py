from django import forms
from django.core.validators import MinValueValidator
from decimal import Decimal
from .models import Account, Transaction, FixedRate
from users.models import Category
from django.shortcuts import get_object_or_404


class AccountForm(forms.ModelForm):
    KIND_CHOICES = [
        ("1", "Banco"),
        ("2", "Corretora"),
        ("3", "Cartão"),
    ]

    balance_cents = forms.DecimalField(decimal_places=2, max_digits=10)
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
    account = forms.ModelChoiceField(
        queryset=Account.objects.all(), widget=forms.HiddenInput()
    )

    def __init__(self, *args, **kwargs):
        self.account_id = kwargs.pop("account_id", None)
        user_id = kwargs.pop("user_id", None)
        super().__init__(*args, **kwargs)
        if self.instance.pk:  # if this is an update
            self.fields["date"].disabled = True
            self.fields["value_cents"].disabled = True
            self.fields["kind"].disabled = True
        self.fields["category"].queryset = Category.objects.filter(user=user_id)
        self.fields["category"].required = False  # Make category optional
        account = get_object_or_404(Account, pk=self.account_id)
        self.fields["account"].initial = account

    class Meta:
        model = Transaction
        fields = [
            "date",
            "value_cents",
            "description",
            "kind",
            "category",
            "account",
        ]


class FixedRateForm(forms.ModelForm):
    invested_cents = forms.DecimalField(
        decimal_places=2, max_digits=10, validators=[MinValueValidator(Decimal("0.01"))]
    )
    current_balance_cents = forms.DecimalField(
        decimal_places=2, max_digits=10, validators=[MinValueValidator(Decimal("0.01"))]
    )
    account_id = forms.IntegerField(widget=forms.HiddenInput())

    def __init__(self, *args, **kwargs):
        self.account_id = kwargs.pop("account_id", None)
        super().__init__(*args, **kwargs)
        self.fields["account_id"].initial = self.account_id

    class Meta:
        model = FixedRate
        fields = [
            "name",
            "invested_cents",
            "current_balance_cents",
            "account_id",
        ]
