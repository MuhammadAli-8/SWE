# Generated by Django 4.2.17 on 2024-12-20 20:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_orderitem_status_shipping'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shipping',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shipping_details', to='orders.cart'),
        ),
    ]