from django import forms

from .models import Taxes


class TaxForm(forms.ModelForm):
    class Meta:
        model = Taxes
        fields = ["description", "percentage", "scope", "tax_amount"]
