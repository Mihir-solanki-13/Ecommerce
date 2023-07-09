# Generated by Django 4.2.2 on 2023-07-08 12:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("seller", "0001_initial"),
        ("products", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="seller",
            field=models.ForeignKey(
                default="6ba7b810-9dad-11d1-80b4-00c04fd430c8",
                on_delete=django.db.models.deletion.CASCADE,
                related_name="products",
                to="seller.seller",
            ),
            preserve_default=False,
        ),
    ]
