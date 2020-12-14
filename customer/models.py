from django.db import models
from django.contrib.auth.models import User
import random
# Create your models here.

GeneralStatus = (
    ('st1', 'В обработке'),
    ('st2', 'Одобрено'),
)

LoanStatus = (
    ('st1', 'Занял'),
    ('st2', 'Вернул'),
)

CurrencyType = (
    ('USD', 'USD'),
    ('RUB', 'RUB'),
    ('UZS', 'UZS'),
)

ServiceType = (
    ('st1', 'За долги'),
    ('st2', 'За перевозку Москва-Ташкент'),
    ('st3', 'За перевозку Ташкент-Москва'),
    ('st4', 'За Товар'),
)

PlanType = (
    ('st1', 'Эконом Москва-Ташкент'),
    ('st2', 'Эконом Ташкент-Москва'),
    ('st3', 'Стандарт Москва-Ташкент'),
    ('st4', 'Стандарт Ташкент-Москва'),
    ('st5', 'Ултрасрочный Москва-Ташкент'),
    ('st6', 'Ултрасрочный Ташкент-Москва'),
    ('st7', 'Духи Москва-Ташкент'),
    ('st8', 'Лекарство Москва-Ташкент'),
)


# customerning balansini tuldirishlari istoriyasi
class CustomerAccountHistory(models.Model):
    uniq_id = models.CharField(max_length=50, default='00')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    usd = models.FloatField(max_length=255, default='00')
    # rub = models.FloatField(max_length=255, default='00')
    # uzs = models.FloatField(max_length=255, default='00')
    staff_id = models.CharField(max_length=50, default='00')
    courier_id = models.CharField(max_length=50, default='00')
    description = models.CharField(max_length=255, default='00')
    # currency_type = models.CharField(max_length=50, choices=CurrencyType, null=False, default=True)
    general_status = models.CharField(max_length=50, choices=GeneralStatus, default='В обработке')
    date_created = models.DateField(auto_now_add=True, blank=True)
    date_updated = models.DateField(auto_now=True, blank=True)

    def __str__(self):
        return str(self.user)


# customerning umumiy balans puli tepadagi tablisa yigindisi-summasi
class CustomerAccount(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    usd = models.FloatField(max_length=255, default='00')
    date_created = models.DateField(auto_now_add=True, blank=True)
    date_updated = models.DateField(auto_now=True, blank=True)

    def __str__(self):
        return self.user


# customerdan ketgan pullar-harajatlar istoriyasi
class CustomerExpensesHistory(models.Model):
    uniq_id = models.CharField(max_length=50, default='00')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    usd = models.FloatField(max_length=255, default='00')
    staff_id = models.CharField(max_length=50, default='00')
    description = models.CharField(max_length=255, default='00')
    service_type = models.CharField(max_length=50, choices=ServiceType, default='00')
    plan_type = models.CharField(max_length=50, choices=PlanType, default='00')
    date_created = models.DateField(auto_now_add=True, blank=True)
    date_updated = models.DateField(auto_now=True, blank=True)

    def __str__(self):
        return str(self.user)


# customerning umumiy harajati tepadagi janvalni yigindisi
class CustomerExpenses(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    usd = models.FloatField(max_length=255, default='00')
    date_created = models.DateField(auto_now_add=True, blank=True)
    date_updated = models.DateField(auto_now=True, blank=True)

    def __str__(self):
        return self.user


# customer olgan qarzlar istoriyasi
class CustomerLoanHistory(models.Model):
    uniq_id = models.CharField(max_length=50, default='00')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    usd = models.FloatField(max_length=255, default='00')
    staff_id = models.CharField(max_length=50, default='00')
    description = models.CharField(max_length=255, default='00')
    general_status = models.CharField(max_length=50, choices=GeneralStatus, null=False, default='В обработке')
    loan_status = models.CharField(max_length=50, choices=LoanStatus, default='Взял')
    date_created = models.DateField(auto_now_add=True, blank=True)
    date_updated = models.DateField(auto_now=True, blank=True)

    def __str__(self):
        return str(self.user)


# customerning umumiy qarzlari yigindisi
class CustomerLoan(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    usd = models.FloatField(max_length=255, default='00')
    date_created = models.DateField(auto_now_add=True, blank=True)
    date_updated = models.DateField(auto_now=True, blank=True)

    def __str__(self):
        return self.user