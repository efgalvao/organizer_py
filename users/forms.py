from django import forms
from django.core.validators import MinValueValidator
from decimal import Decimal
from .models import Category, Financing, Installment, Transference
from Services.account_services import AccountServices
from account.models import Account


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["name"]


class FinancingForm(forms.ModelForm):
    borrowed_value_cents = forms.DecimalField(
        decimal_places=2, max_digits=10, validators=[MinValueValidator(Decimal("0.01"))]
    )

    class Meta:
        model = Financing
        fields = ["name", "borrowed_value_cents", "parcels"]


class InstallmentForm(forms.ModelForm):
    amortization_cents = forms.DecimalField(
        decimal_places=2, max_digits=10, validators=[MinValueValidator(Decimal("0.01"))]
    )
    interest_cents = forms.DecimalField(
        decimal_places=2, max_digits=10, validators=[MinValueValidator(Decimal("0.01"))]
    )
    insurance_cents = forms.DecimalField(
        decimal_places=2, max_digits=10, validators=[MinValueValidator(Decimal("0.01"))]
    )
    fees_cents = forms.DecimalField(
        decimal_places=2, max_digits=10, validators=[MinValueValidator(Decimal("0.01"))]
    )
    monetary_correction_cents = forms.DecimalField(
        decimal_places=2, max_digits=10, validators=[MinValueValidator(Decimal("0.01"))]
    )
    adjustment_cents = forms.DecimalField(
        decimal_places=2, max_digits=10, validators=[MinValueValidator(Decimal("0.01"))]
    )

    class Meta:
        model = Installment
        fields = [
            "ordinary",
            "parcel",
            "paid_parcels",
            "payment_date",
            "amortization_cents",
            "interest_cents",
            "insurance_cents",
            "fees_cents",
            "monetary_correction_cents",
            "adjustment_cents",
        ]


class TransferenceForm(forms.ModelForm):
    value_cents = forms.DecimalField(
        decimal_places=2, max_digits=10, validators=[MinValueValidator(Decimal("0.01"))]
    )

    receiver = forms.ModelChoiceField(queryset=Account.objects.none())
    sender = forms.ModelChoiceField(queryset=Account.objects.none())

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop("user", None)
        super(TransferenceForm, self).__init__(*args, **kwargs)
        if self.user:
            self.fields["receiver"].queryset = AccountServices.fetch_accounts_for_user(
                self.user
            )
            self.fields["sender"].queryset = AccountServices.fetch_accounts_for_user(
                self.user
            )

    def clean(self):
        cleaned_data = super().clean()
        sender = cleaned_data.get("sender")
        receiver = cleaned_data.get("receiver")

        if sender and receiver:
            if sender == receiver:
                raise forms.ValidationError("Sender and receiver cannot be the same.")

        return cleaned_data

    class Meta:
        model = Transference
        fields = ["sender", "receiver", "value_cents", "date"]
