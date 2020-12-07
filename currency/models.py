from django.db import models
from django.contrib.auth.models import User
# Create your models here.


# currncy tuldirishlari istoriyasi
class CurrencyHistory(models.Model):
    usd_rub = models.FloatField(max_length=255, default='00')
    usd_uzs = models.FloatField(max_length=255, default='00')
    # uzs = models.FloatField(max_length=255, default='00')
    date_created = models.DateField(auto_now_add=True, blank=True)
    date_updated = models.DateField(auto_now=True, blank=True)

    def __str__(self):
        return str(self.usd)