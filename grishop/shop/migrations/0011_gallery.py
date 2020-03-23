# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-03-23 13:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_product_new_tovar'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_gallery', models.CharField(max_length=400, verbose_name='название фото')),
                ('photo_gallery', models.ImageField(blank=True, upload_to='gallery', verbose_name='фото')),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Фотогаллерея',
                'verbose_name_plural': 'Фотогаллерея',
            },
        ),
    ]
