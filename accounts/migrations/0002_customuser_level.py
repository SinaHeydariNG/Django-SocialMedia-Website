# Generated by Django 4.1.1 on 2022-09-21 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='level',
            field=models.CharField(choices=[('BRONZE', 'BRONZE'), ('SILVER', 'SILVER'), ('GOLD', 'GOLD')], default='BRONZE', max_length=10),
        ),
    ]
