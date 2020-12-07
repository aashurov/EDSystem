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
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uniq_id', models.CharField(default='00', max_length=50)),
                ('phone_number', models.CharField(default='phone_number', max_length=255)),
                ('address_first', models.CharField(default='address_first', max_length=255)),
                ('address_second', models.CharField(default='address_second', max_length=255)),
                ('passport_number', models.CharField(default='passport_number', max_length=255)),
                ('passport_date_first', models.DateField(blank=True, null=True)),
                ('passport_date_second', models.DateField(blank=True, null=True)),
                ('passport_organization', models.CharField(default='passport_organization', max_length=255)),
                ('user_organization', models.CharField(default='user_organization', max_length=255)),
                ('description', models.CharField(default='description', max_length=255)),
                ('is_official', models.BooleanField(default=True)),
                ('role', models.CharField(choices=[('администратор', 'администратор'), ('менеджер', 'менеджер'), ('курер', 'курер'), ('клиент', 'клиент')], default='клиент', max_length=50)),
                ('avatar_image', models.ImageField(default='avatar.png', upload_to='photos/%Y/%m/%d/')),
                ('passport_image', models.ImageField(default='passport_image.png', upload_to='photos/%Y/%m/%d/')),
                ('passport_image_behind', models.ImageField(default='passport_image_behind.png', upload_to='photos/%Y/%m/%d/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
