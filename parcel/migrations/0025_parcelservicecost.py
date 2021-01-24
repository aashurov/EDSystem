# Generated by Django 3.1.3 on 2021-01-24 19:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('parcel', '0024_auto_20210124_1831'),
    ]

    operations = [
        migrations.CreateModel(
            name='ParcelServiceCost',
            fields=[
                ('parcelmain', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='parcel.parcelmain')),
                ('service_type', models.CharField(default='00', max_length=255)),
                ('service_cost', models.FloatField(default='00', max_length=50)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('date_updated', models.DateField(auto_now=True)),
                ('courier_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='courier_id', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
