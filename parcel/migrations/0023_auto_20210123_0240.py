# Generated by Django 3.1.3 on 2021-01-23 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parcel', '0022_auto_20210123_0228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parcelmain',
            name='parcel_getmoney_foritem',
            field=models.CharField(default='00', max_length=255),
        ),
    ]