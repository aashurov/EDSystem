# Generated by Django 3.1.3 on 2020-12-13 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0004_auto_20201213_1150'),
    ]

    operations = [
        migrations.AddField(
            model_name='companyaccounthistory',
            name='description',
            field=models.CharField(default='00', max_length=255),
        ),
        migrations.AddField(
            model_name='companyexpenseshistory',
            name='description',
            field=models.CharField(default='00', max_length=255),
        ),
        migrations.AddField(
            model_name='companyownexpenseshistory',
            name='description',
            field=models.CharField(default='00', max_length=255),
        ),
    ]
