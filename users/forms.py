from django import forms
from django.core.validators import MinValueValidator
from decimal import Decimal
from .models import Category, Financing


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
        fields = ["name", "borrowed_value_cents", "installments"]
