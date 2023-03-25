from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.postgres import fields as PostgresFields


class ProductCategory(models.Model):
    name = models.CharField(max_length=256)
    icon_url = models.URLField(blank=True)
    description = models.TextField()
    parent_category = models.ForeignKey(
        "self",
        blank=True,
        null=True,
        related_name="children_categories",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name


class Maker(models.Model):
    name = models.CharField(max_length=512)

    def __str__(self):
        return self.name


class Product(models.Model):
    class Currency(models.TextChoices):
        REAL = ("RS", _("Reais"))  # real brasileiro
        BITCOIN = ("BTC", _("Bitcoin"))

    name = models.CharField(max_length=512)
    subtitle = models.CharField(max_length=512)
    maker = models.ForeignKey(
        Maker,
        on_delete=models.CASCADE,  # ao um maker ser deletado, todos os produtos tb são!
        related_name="products",
        blank=True,
        null=True,
    )
    image1 = models.ImageField(blank=True, null=True)
    image2 = models.ImageField(blank=True, null=True)
    image3 = models.ImageField(blank=True, null=True)
    image4 = models.ImageField(blank=True, null=True)
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )
    currency = models.TextField(
        default=Currency.REAL,
        choices=Currency.choices,
        max_length=3,
    )
    variation_product_id = PostgresFields.ArrayField(
        models.IntegerField(null=True, blank=True),
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"{self.name} - {self.subtitle} - {self.maker}"
