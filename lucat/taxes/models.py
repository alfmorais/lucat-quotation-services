from django.db import models


class Taxes(models.Model):
    SCOPE_CHOICES = [
        ("ESTADUAL", "Estadual"),
        ("FEDERAL", "Federal"),
        ("TAXA", "Taxa"),
    ]

    description = models.CharField(
        max_length=128,
        verbose_name="Descrição do Imposto",
    )
    percentage = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        verbose_name="Porcentagem do impostos",
    )
    scope = models.CharField(
        max_length=10,
        choices=SCOPE_CHOICES,
        verbose_name="Escopo do imposto: Estadual, Federal ou Taxa",
    )
    tax_amount = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=0.0,
        verbose_name="Valor da Taxa quase não seja calculado pela porcentagem",
    )

    def __str__(self):
        return (
            f"[Taxes ID: {self.id}, "
            f"Description: {self.description} / "
            f"{self.percentage}% or {self.tax_amount}]"
        )
