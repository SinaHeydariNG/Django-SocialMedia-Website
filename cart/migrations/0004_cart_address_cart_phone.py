# Generated by Django 4.1.1 on 2022-09-24 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_alter_cart_order_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='address',
            field=models.CharField(blank=True, max_length=225, null=True),
        ),
        migrations.AddField(
            model_name='cart',
            name='phone',
            field=models.CharField(blank=True, max_length=225, null=True),
        ),
    ]
