from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from .forms import ProductForm
from .models import Products


class ProductListView(ListView):
    model = Products
    template_name = "products/list.html"
    context_object_name = "products"


class ProductDetailView(DetailView):
    model = Products
    template_name = "products/detail.html"
    context_object_name = "product"


class ProductCreateView(CreateView):
    model = Products
    form_class = ProductForm
    template_name = "products/form.html"
    success_url = reverse_lazy("product-list")


class ProductUpdateView(UpdateView):
    model = Products
    form_class = ProductForm
    template_name = "products/form.html"
    success_url = reverse_lazy("product-list")


class ProductDeleteView(DeleteView):
    model = Products
    template_name = "products/delete.html"
    success_url = reverse_lazy("product-list")
