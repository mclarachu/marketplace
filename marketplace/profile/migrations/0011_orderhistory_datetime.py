# Generated by Django 3.0.5 on 2020-04-21 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0010_auto_20200421_0144'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderhistory',
            name='dateTime',
            field=models.DateTimeField(auto_now=True),
        ),
    ]