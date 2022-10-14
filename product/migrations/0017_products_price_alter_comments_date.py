# Generated by Django 4.1.1 on 2022-09-24 14:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0016_alter_comments_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='price',
            field=models.DecimalField(decimal_places=2, default=100, max_digits=6),
        ),
        migrations.AlterField(
            model_name='comments',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 24, 7, 51, 54, 706766)),
        ),
    ]
