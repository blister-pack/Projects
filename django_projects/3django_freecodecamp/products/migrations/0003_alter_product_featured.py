# Generated by Django 4.2.6 on 2023-10-16 19:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0002_product_featured"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="featured",
            field=models.BooleanField(default=False),
        ),
    ]
