# Generated by Django 3.1.3 on 2021-01-21 01:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('parcel', '0015_auto_20210120_2102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parcelmain',
            name='parcel_plan',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parcel_plan', to='parcel.parcelplan'),
        ),
    ]
