# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-06-10 20:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0025_auto_20200531_1650'),
    ]

    operations = [
        migrations.CreateModel(
            name='Raiting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=15, verbose_name='IP адрес')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Product', verbose_name='товар')),
            ],
            options={
                'verbose_name': 'Рейтинг',
                'verbose_name_plural': 'Рейтинги',
            },
        ),
        migrations.CreateModel(
            name='RaitingStar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.SmallIntegerField(default=0, verbose_name='значение')),
            ],
            options={
                'verbose_name': 'звезда рейтинга',
                'verbose_name_plural': 'звёзды рейтинга',
                'ordering': ['-value'],
            },
        ),
        migrations.AddField(
            model_name='raiting',
            name='star',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.RaitingStar', verbose_name='звезда'),
        ),
    ]