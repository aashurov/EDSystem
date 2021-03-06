# Generated by Django 3.1.3 on 2021-01-07 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ParcelPlan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uniq_id', models.CharField(default='00', max_length=50)),
                ('parcel_name', models.CharField(default='00', max_length=50)),
                ('parcel_price', models.FloatField(default='00', max_length=255)),
                ('description', models.CharField(default='00', max_length=255)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('date_updated', models.DateField(auto_now=True)),
            ],
        ),
    ]
