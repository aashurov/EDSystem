# Generated by Django 3.1.3 on 2020-12-05 18:13

from django.db import migrations, models
import userprofile.models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='uniq_id',
            field=models.CharField(default=userprofile.models.create_uniq_id, max_length=50),
        ),
    ]
