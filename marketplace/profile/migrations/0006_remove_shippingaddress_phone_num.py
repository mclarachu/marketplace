# Generated by Django 3.0.5 on 2020-04-21 11:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0005_auto_20200421_0921'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shippingaddress',
            name='phone_num',
        ),
    ]
