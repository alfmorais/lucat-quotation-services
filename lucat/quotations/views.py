from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView

from .forms import QuotationItemFormSet
from .models import Quotation


class QuotationListView(ListView):
    model = Quotation
    template_name = "quotations/list.html"
    context_object_name = "quotations"


class QuotationCreateView(CreateView):
    model = Quotation
    fields = []
    template_name = "quotations/form.html"
    success_url = reverse_lazy("quotation_list")

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)

        match bool(self.request.POST):
            case True:
                data["formset"] = QuotationItemFormSet(self.request.POST)
            case False:
                data["formset"] = QuotationItemFormSet()

        return data

    def form_valid(self, form):
        formset = self.get_context_data()["formset"]

        if formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return redirect(self.success_url)

        return self.form_invalid(form)


class QuotationUpdateView(UpdateView):
    model = Quotation
    fields = []
    template_name = "quotations/form.html"
    success_url = reverse_lazy("quotation_list")

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)

        match bool(self.request.POST):
            case True:
                data["formset"] = QuotationItemFormSet(
                    self.request.POST,
                    instance=self.object,
                )
            case False:
                data["formset"] = QuotationItemFormSet(instance=self.object)

        return data

    def form_valid(self, form):
        formset = self.get_context_data()["formset"]

        if formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return redirect(self.success_url)

        return self.form_invalid(form)
