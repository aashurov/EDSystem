# Generated by Django 3.1.3 on 2021-01-20 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parcel', '0014_auto_20210118_1640'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='parcelitems',
            name='prod_image',
        ),
        migrations.AlterField(
            model_name='parcelmain',
            name='parcel_image',
            field=models.ImageField(blank=True, default='no-photo.png', null=True, upload_to='photos/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='parcelmain',
            name='parcel_report_image',
            field=models.ImageField(blank=True, default='no-photo.png', null=True, upload_to='photos/%Y/%m/%d/'),
        ),
    ]
