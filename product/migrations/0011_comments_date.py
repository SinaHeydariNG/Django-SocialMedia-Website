# Generated by Django 4.1.1 on 2022-09-20 17:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0010_comments_parent'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 20, 10, 14, 47, 400921)),
        ),
    ]
