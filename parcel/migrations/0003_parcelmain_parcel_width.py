# Generated by Django 3.1.3 on 2021-01-13 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parcel', '0002_parcelitems_parcelmain_parcelstatushistory'),
    ]

    operations = [
        migrations.AddField(
            model_name='parcelmain',
            name='parcel_width',
            field=models.FloatField(default='00', max_length=50),
        ),
    ]