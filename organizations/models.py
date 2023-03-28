from django.db import models

from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _

from products.models import Product



class OrganizationCategory(models.Model):
    name = models.CharField(max_length=256)
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


class Owner(models.Model):
    name = models.CharField(max_length=512)
    cpf = models.CharField(max_length=16)
    cpf_regex = RegexValidator(r'^\d{11}$', 'Ingrese un CPF válido de 11 dígitos')
    cpf = models.CharField(validators=[cpf_regex], max_length=11, unique=True)

    def __str__(self):
        return self.name


class Organization(models.Model):
    class Localization(models.TextChoices):
        CURURUPU = ("CPU", _("Cururupu"))
        PINHEIRO = ("PHO", _("Pinheiro"))

    name = models.CharField(max_length=512)
    descripton = models.CharField(max_length=512)
    localization = models.TextField(
        default=Localization.CURURUPU,
        choices=Localization.choices,
        max_length=3,
    )
    owner = models.ForeignKey(
        Owner,
        on_delete=models.CASCADE,
        related_name="organizations",
        blank=True,
        null=True,
    )
    products = models.ManyToManyField(
        Product,
        related_name="organizations",
        blank=True,
    )
    image1 = models.ImageField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.descripton} - {self.localization}"
