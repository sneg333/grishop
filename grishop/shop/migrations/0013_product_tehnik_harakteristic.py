# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-03-23 19:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0012_product_product_gallery'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='tehnik_harakteristic',
            field=models.TextField(blank=True, verbose_name='Технические характеристики'),
        ),
    ]
