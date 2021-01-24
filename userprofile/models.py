import random
from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from customer.models import *
from staff.models import *
from datetime import date, datetime
import uuid
from django.db.models import Max
Roles = (
    ('администратор', 'администратор'),
    ('менеджер', 'менеджер'),
    ('курер', 'курер'),
    ('клиент', 'клиент'),
)

def create_uniq_id():
    userid=User.objects.all().order_by('id').last()
    userid.id = userid.id
    return '%05d' % userid.id

# general_uniq_id = str(random.randint(1000, 9999))
class UserProfile(models.Model):
    objects = models.Manager()
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    uniq_id = models.CharField(max_length=50, default=create_uniq_id)
    phone_number = models.CharField(max_length=255, default='phone_number')
    address_first = models.CharField(max_length=255, default='address_first')
    address_second = models.CharField(max_length=255, default='address_second')
    passport_number = models.CharField(max_length=255, default='passport_number')
    passport_date_first = models.DateField(null=True, blank=True)
    passport_date_second = models.DateField(null=True, blank=True)
    passport_organization = models.CharField(max_length=255, default='passport_organization')
    user_organization = models.CharField(max_length=255, default='user_organization')
    description = models.CharField(max_length=255, default='description')
    is_official = models.BooleanField(default=True)
    role = models.CharField(max_length=50, choices=Roles, default='клиент')
    avatar_image = models.ImageField(upload_to='photos/%Y/%m/%d/', default='avatar.png')
    passport_image = models.ImageField(upload_to='photos/%Y/%m/%d/', default='no-photo.png')
    passport_image_behind = models.ImageField(upload_to='photos/%Y/%m/%d/', default='no-photo.png')



    # def save(self, *args, **kwargs):
    #     if not self.uniq_id:
    #         self.uniq_id = 'A%05d' % self.id
    #         super().save(*args, **kwargs)

    # def save(self, **kwargs):
    #     if not self.uniq_id:
    #         self.uniq_id = "A%05d" % self.id
    #     super().save(*kwargs)
    #
    #
    # @property
    # def sid(self):
    #     self.uniq_id = "A%05d" % self.id
    #     return self.uniq_id

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
        CustomerAccount.objects.create(user=instance)
        CustomerLoan.objects.create(user=instance)
        CustomerExpenses.objects.create(user=instance)
    instance.customeraccount.save()
    instance.customerloan.save()
    instance.customerexpenses.save()
    instance.userprofile.save()