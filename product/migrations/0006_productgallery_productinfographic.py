# Generated by Django 4.1.1 on 2022-09-19 13:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_productfeatured'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductGallery',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('product.products',),
        ),
        migrations.CreateModel(
            name='ProductInfographic',
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
