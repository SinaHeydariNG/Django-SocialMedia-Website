# Generated by Django 4.1.1 on 2022-09-19 13:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_collections_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductFeatured',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('product.products',),
        ),
    ]