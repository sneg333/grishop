# Generated by Django 3.0.7 on 2020-07-07 18:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0031_auto_20200704_1129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='product_com',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.Product'),
        ),
    ]