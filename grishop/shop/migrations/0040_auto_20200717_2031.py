# Generated by Django 3.0.8 on 2020-07-17 20:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0039_product_brend'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='brend',
        ),
        migrations.DeleteModel(
            name='Brend',
        ),
    ]
