# Generated by Django 4.1.1 on 2022-09-19 12:33

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_products_category_alter_products_collection'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='information',
            field=ckeditor.fields.RichTextField(default='TEST'),
        ),
    ]
