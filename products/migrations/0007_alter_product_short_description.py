# Generated by Django 5.1.4 on 2025-01-23 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_product_short_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='short_description',
            field=models.TextField(blank=True, max_length=300),
        ),
    ]
