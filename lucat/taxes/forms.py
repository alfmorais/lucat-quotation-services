from django import forms

from .models import Taxes


class TaxForm(forms.ModelForm):
    class Meta:
        model = Taxes
        fields = ["description", "percentage", "scope", "tax_amount"]
        widgets = {
            "description": forms.TextInput(attrs={"class": "form-control"}),
            "scope": forms.Select(attrs={"class": "form-control"}),
            "percentage": forms.NumberInput(attrs={"class": "form-control"}),
            "tax_amount": forms.NumberInput(attrs={"class": "form-control"}),
        }
