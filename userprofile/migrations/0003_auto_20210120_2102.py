# Generated by Django 3.1.3 on 2021-01-20 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0002_auto_20201205_1813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='passport_image',
            field=models.ImageField(default='no-photo.png', upload_to='photos/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='passport_image_behind',
            field=models.ImageField(default='no-photo.png', upload_to='photos/%Y/%m/%d/'),
        ),
    ]
