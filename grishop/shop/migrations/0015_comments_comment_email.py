# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-03-24 19:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0014_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='comment_email',
            field=models.EmailField(blank=True, default=None, max_length=254, null=True),
        ),
    ]
