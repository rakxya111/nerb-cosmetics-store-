# Generated by Django 5.1.4 on 2025-01-19 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainshop', '0005_alter_brand_brand_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_sale',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='sale_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
    ]
