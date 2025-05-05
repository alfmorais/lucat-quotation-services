from django import forms

from .models import Products


class ProductForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ["name", "description", "ncm_code", "price"]
        widgets = {
            "name": forms.TextInput(
                attrs={"class": "form-control"},
            ),
            "description": forms.Textarea(
                attrs={"class": "form-control", "rows": 3},
            ),
            "ncm_code": forms.TextInput(
                attrs={"class": "form-control"},
            ),
            "price": forms.NumberInput(
                attrs={"class": "form-control"},
            ),
        }
