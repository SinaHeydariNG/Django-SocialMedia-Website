# Generated by Django 4.1.1 on 2022-09-24 15:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0017_products_price_alter_comments_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 24, 8, 6, 42, 156891)),
        ),
    ]
