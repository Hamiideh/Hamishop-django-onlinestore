# Generated by Django 5.1.4 on 2025-01-23 00:09

import ckeditor.fields
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_alter_comment_datetime_created_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='short_description',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='product',
            name='datetime_created',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date Time of Creation'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
