# Generated by Django 3.1.3 on 2021-01-15 17:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parcel', '0007_parcelitems_prod_weight'),
    ]

    operations = [
        migrations.RenameField(
            model_name='parcelstatushistory',
            old_name='parcelmain',
            new_name='parcelmain_id',
        ),
    ]
