# Generated by Django 5.1.3 on 2024-11-07 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_order_product_order_quantity'),
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='product',
        ),
        migrations.AddField(
            model_name='order',
            name='product',
            field=models.ManyToManyField(to='product.product'),
        ),
    ]
