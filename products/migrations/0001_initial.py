# Generated by Django 4.1.7 on 2023-03-28 15:14

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Maker",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=512)),
            ],
        ),
        migrations.CreateModel(
            name="ProductCategory",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=256)),
                ("icon_url", models.URLField(blank=True)),
                ("description", models.TextField()),
                (
                    "parent_category",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="children_categories",
                        to="products.productcategory",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=512)),
                ("subtitle", models.CharField(max_length=512)),
                ("image1", models.ImageField(blank=True, null=True, upload_to="")),
                ("image2", models.ImageField(blank=True, null=True, upload_to="")),
                ("image3", models.ImageField(blank=True, null=True, upload_to="")),
                ("image4", models.ImageField(blank=True, null=True, upload_to="")),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "currency",
                    models.TextField(
                        choices=[("RS", "Reais"), ("BTC", "Bitcoin")],
                        default="RS",
                        max_length=3,
                    ),
                ),
                (
                    "variation_product_id",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.IntegerField(blank=True, null=True),
                        blank=True,
                        null=True,
                        size=None,
                    ),
                ),
                (
                    "maker",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="products",
                        to="products.maker",
                    ),
                ),
            ],
        ),
    ]
