# Generated by Django 3.1.3 on 2020-12-13 12:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0005_auto_20201213_1156'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='companyownexpenseshistory',
            name='currency_type',
        ),
    ]
