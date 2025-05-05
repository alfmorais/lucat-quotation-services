from django.db import models
from products.models import Products


class Quotation(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"[Quotation ID: {self.id}]"


class QuotationItem(models.Model):
    quotation = models.ForeignKey(
        Quotation,
        related_name="items",
        on_delete=models.CASCADE,
        verbose_name="Cotação",
    )
    product = models.ForeignKey(
        Products,
        on_delete=models.CASCADE,
        verbose_name="Produtos",
    )
    quantity = models.PositiveIntegerField(
        verbose_name="Quantidade de itens no produto",
    )
    unit_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )

    def total(self):
        return self.quantity * self.unit_price

    def __str__(self):
        return f"[QuotationItem ID: {self.id}]"
