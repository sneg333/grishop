# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-04-09 19:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0023_carusel'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='carusel_tovar',
            field=models.BooleanField(default=False, verbose_name='карусель'),
        ),
    ]