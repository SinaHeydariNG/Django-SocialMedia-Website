# Generated by Django 4.1.2 on 2022-10-14 10:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0025_alter_comments_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 14, 6, 37, 47, 657937)),
        ),
    ]
