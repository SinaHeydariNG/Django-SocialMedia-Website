# Generated by Django 4.1.1 on 2022-09-20 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_siteinfo_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Navbar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=225)),
                ('url', models.URLField()),
            ],
        ),
    ]
