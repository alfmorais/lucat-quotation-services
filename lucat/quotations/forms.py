from django import forms
from django.forms.models import inlineformset_factory

from .models import Quotation, QuotationItem


class QuotationItemForm(forms.ModelForm):
    class Meta:
        model = QuotationItem
        fields = ["product", "quantity", "unit_price"]


QuotationItemFormSet = inlineformset_factory(
    Quotation, QuotationItem, form=QuotationItemForm, extra=1, can_delete=True
)
