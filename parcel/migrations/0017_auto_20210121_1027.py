# Generated by Django 3.1.3 on 2021-01-21 10:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parcel', '0016_auto_20210121_0124'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='parcelmain',
            name='parcel_dostavka',
        ),
        migrations.RemoveField(
            model_name='parcelmain',
            name='parcel_zabor',
        ),
    ]