from django.db import models


class Products(models.Model):
    name = models.CharField(
        max_length=128,
        unique=True,
        verbose_name="Identificação do produto",
    )
    description = models.TextField(
        verbose_name="Descrição detalhada do produto",
    )
    ncm_code = models.CharField(
        max_length=16,
        verbose_name="Código NCM",
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Preço unitário do produto",
    )

    def __str__(self):
        return f"[Product ID: {self.id}, Name: {self.name}]"
