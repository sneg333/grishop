# Generated by Django 3.0.7 on 2020-07-11 11:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0033_auto_20200709_1807'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Raiting',
        ),
        migrations.DeleteModel(
            name='RaitingStar',
        ),
    ]