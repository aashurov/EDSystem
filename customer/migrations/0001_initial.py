# Generated by Django 3.1.3 on 2020-12-05 15:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerLoanHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uniq_id', models.CharField(default='00', max_length=50)),
                ('usd', models.FloatField(default='00', max_length=255)),
                ('rub', models.FloatField(default='00', max_length=255)),
                ('uzs', models.FloatField(default='00', max_length=255)),
                ('currency_type', models.CharField(choices=[('USD', 'USD'), ('RUB', 'RUB'), ('UZS', 'UZS')], default=True, max_length=50)),
                ('general_status', models.CharField(choices=[('st1', 'В обработке'), ('st2', 'Одобрено')], default='В обработке', max_length=50)),
                ('loan_status', models.CharField(choices=[('st1', 'Занял'), ('st2', 'Вернул')], default='Взял', max_length=50)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('date_updated', models.DateField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CustomerLoan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usd', models.FloatField(default='00', max_length=255)),
                ('rub', models.FloatField(default='00', max_length=255)),
                ('uzs', models.FloatField(default='00', max_length=255)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('date_updated', models.DateField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CustomerExpensesHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uniq_id', models.CharField(default='00', max_length=50)),
                ('usd', models.FloatField(default='00', max_length=255)),
                ('rub', models.FloatField(default='00', max_length=255)),
                ('uzs', models.FloatField(default='00', max_length=255)),
                ('currency_type', models.CharField(choices=[('USD', 'USD'), ('RUB', 'RUB'), ('UZS', 'UZS')], default=True, max_length=50)),
                ('service_type', models.CharField(choices=[('st1', 'За долги'), ('st2', 'За перевозку Москва-Ташкент'), ('st3', 'За перевозку Ташкент-Москва'), ('st4', 'За Товар')], default='00', max_length=50)),
                ('plan_type', models.CharField(choices=[('st1', 'Эконом Москва-Ташкент'), ('st2', 'Эконом Ташкент-Москва'), ('st3', 'Стандарт Москва-Ташкент'), ('st4', 'Стандарт Ташкент-Москва'), ('st5', 'Ултрасрочный Москва-Ташкент'), ('st6', 'Ултрасрочный Ташкент-Москва'), ('st7', 'Духи Москва-Ташкент'), ('st8', 'Лекарство Москва-Ташкент')], default='00', max_length=50)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('date_updated', models.DateField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CustomerExpenses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usd', models.FloatField(default='00', max_length=255)),
                ('rub', models.FloatField(default='00', max_length=255)),
                ('uzs', models.FloatField(default='00', max_length=255)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('date_updated', models.DateField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CustomerAccountHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uniq_id', models.CharField(default='00', max_length=50)),
                ('usd', models.FloatField(default='00', max_length=255)),
                ('rub', models.FloatField(default='00', max_length=255)),
                ('uzs', models.FloatField(default='00', max_length=255)),
                ('currency_type', models.CharField(choices=[('USD', 'USD'), ('RUB', 'RUB'), ('UZS', 'UZS')], default=True, max_length=50)),
                ('general_status', models.CharField(choices=[('st1', 'В обработке'), ('st2', 'Одобрено')], default='В обработке', max_length=50)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('date_updated', models.DateField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CustomerAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usd', models.FloatField(default='00', max_length=255)),
                ('rub', models.FloatField(default='00', max_length=255)),
                ('uzs', models.FloatField(default='00', max_length=255)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('date_updated', models.DateField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
