from django.db import models
from django.contrib.auth.models import User
# Create your models here.


# parcel tariflari
class ParcelPlan(models.Model):
    uniq_id = models.CharField(max_length=50, default='00')
    parcel_name = models.CharField(max_length=50, default='00')
    parcel_price = models.FloatField(max_length=255, default='00')
    description = models.CharField(max_length=255, default='00')
    date_created = models.DateField(auto_now_add=True, blank=True)
    date_updated = models.DateField(auto_now=True, blank=True)

    def __str__(self):
        return str(self.parcel_name)


class ParcelStatusName(models.Model):
    parcel_status = models.CharField(max_length=255, default='00')
    date_created = models.DateField(auto_now_add=True, blank=True)
    date_updated = models.DateField(auto_now=True, blank=True)

    def __str__(self):
        return str(self.parcel_status)


# parcel tariflari
class ParcelMain(models.Model):
    uniq_id = models.CharField(max_length=50, default='00')
    sender = models.ForeignKey(User, on_delete=models.CASCADE, unique=False,  null=True, related_name='sender')
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, unique=False,  null=True, related_name='recipient')

    staff_sender = models.ForeignKey(User, on_delete=models.CASCADE, unique=False,  null=True, related_name='staff_sender')
    staff_recipient = models.ForeignKey(User, on_delete=models.CASCADE, unique=False,  null=True, related_name='staff_recipient')
    courier_zabor = models.ForeignKey(User, on_delete=models.CASCADE, unique=False,  null=True, related_name='courier_zabor')
    courier_dostavka = models.ForeignKey(User, on_delete=models.CASCADE, unique=False,  null=True, related_name='courier_dostavka')

    parcel_plan = models.ForeignKey(ParcelPlan, on_delete=models.CASCADE, unique=False,  null=True, related_name='parcel_plan')
    parcel_cost = models.FloatField(max_length=255, default='00')
    parcel_item_total_cost = models.FloatField(max_length=255, default='00')
    parcel_getmoney_foritem = models.CharField(max_length=255, default='00')
    parcel_zabor_cost = models.FloatField(max_length=255, default='00')
    parcel_dostavka_cost = models.FloatField(max_length=255, default='00')
    parcel_procent_prod_cost = models.FloatField(max_length=255, default='00')
    parcel_from = models.CharField(max_length=255, default='00')
    parcel_status = models.ForeignKey(ParcelStatusName, on_delete=models.CASCADE, unique=False, null=True, related_name='parcel_status_current')
    parcel_zabor = models.CharField(max_length=255, default='00')
    parcel_dostavka = models.CharField(max_length=255, default='00')
    parcel_length = models.FloatField(max_length=50, default='00')
    parcel_width = models.FloatField(max_length=50, default='00')
    parcel_height = models.FloatField(max_length=50, default='00')
    parcel_dimension = models.FloatField(max_length=50, default='00')
    parcel_weight = models.FloatField(max_length=50, default='00')
    parcel_description = models.CharField(max_length=255, default='00')
    parcel_image = models.ImageField(null=True, blank=True, upload_to='photos/%Y/%m/%d/', default='no-photo.png')
    parcel_report_image = models.ImageField(null=True, blank=True, upload_to='photos/%Y/%m/%d/', default='no-photo.png')

    date_created = models.DateField(auto_now_add=True, blank=True)
    date_updated = models.DateField(auto_now=True, blank=True)

    def __str__(self):
        return str(self.uniq_id)


# parcel itemlari
class ParcelItems(models.Model):
    parcelmain = models.ForeignKey(ParcelMain, on_delete=models.CASCADE, unique=False)
    prod_url = models.CharField(max_length=255, default='00')
    prod_name = models.CharField(max_length=255, default='00')
    prod_cnt = models.FloatField(max_length=50, default='00')
    prod_cost = models.FloatField(max_length=50, default='00')
    prod_total_cost = models.FloatField(max_length=50, default='00')
    prod_tnved = models.CharField(max_length=50, default='00')
    prod_weight = models.FloatField(max_length=50, default='00')
    # prod_image = models.ImageField(null=True, blank=True, upload_to='photos/%Y/%m/%d/', default='passport_image.png')
    date_created = models.DateField(auto_now_add=True, blank=True)
    date_updated = models.DateField(auto_now=True, blank=True)

    def __str__(self):
        return str(self.prod_name)


class ParcelStatusHistory(models.Model):
    parcelmain = models.ForeignKey(ParcelMain, on_delete=models.CASCADE)
    parcel_status = models.ForeignKey(ParcelStatusName, on_delete=models.CASCADE, unique=False, null=True, related_name='parcel_status_history')
    date_created = models.DateField(auto_now_add=True, blank=True)
    date_updated = models.DateField(auto_now=True, blank=True)

    def __str__(self):
        return str(self.parcel_status)

class ParcelImages(models.Model):
    parcelmain = models.ForeignKey(ParcelMain, on_delete=models.CASCADE)
    parcel_image = models.ImageField(null=True, blank=True, upload_to='photos/%Y/%m/%d/', default='passport_image.png')

    def __str__(self):
        return str(self.parcel_image)

