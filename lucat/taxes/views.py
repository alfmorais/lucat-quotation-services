from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from .forms import TaxForm
from .models import Taxes


class TaxListView(ListView):
    model = Taxes
    template_name = "taxes/list.html"
    context_object_name = "taxes"


class TaxCreateView(CreateView):
    model = Taxes
    form_class = TaxForm
    template_name = "taxes/form.html"
    success_url = reverse_lazy("tax-list")


class TaxUpdateView(UpdateView):
    model = Taxes
    form_class = TaxForm
    template_name = "taxes/form.html"
    success_url = reverse_lazy("tax-list")


class TaxDeleteView(DeleteView):
    model = Taxes
    template_name = "taxes/delete.html"
    success_url = reverse_lazy("tax-list")


class TaxDetailView(DetailView):
    model = Taxes
    template_name = "taxes/detail.html"
