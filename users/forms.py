from django import forms
from django.core.validators import MinValueValidator
from decimal import Decimal
from .models import Category, Financing, Installment


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
