from django.db import models
from django.contrib.auth.models import User
from customer.models import *
import random
# Create your models here.

GeneralStatus = (
    ('В обработке', 'В обработке'),
    ('Одобрено', 'Одобрено'),
)

LoanStatus = (
    ('Занял', 'Занял'),
    ('Вернул', 'Вернул'),
)

CurrencyType = (
    ('USD', 'USD'),
    ('RUB', 'RUB'),
    ('UZS', 'UZS'),
)

ServiceType = (
    ('За Товар', 'За Товар'),
    ('За перевозку Москва-Ташкент', 'За перевозку Москва-Ташкент'),
    ('За перевозку Ташкент-Москва', 'За перевозку Ташкент-Москва'),
)

CompanyExpensesType = (
    ('Мелкие расходы', 'Мелкие расходы'),
    ('Зарплата', 'Зарплата'),
    ('Обед', 'Обед'),
    ('Бензин', 'Бензин'),
    ('Еб куйдик', 'Еб куйдик'),
    ('Прочие', 'Прочие'),
    ('За долг', 'За долг'),
)

PlanType = (
    ('Эконом Москва-Ташкент', 'Эконом Москва-Ташкент'),
    ('Эконом Ташкент-Москва', 'Эконом Ташкент-Москва'),
    ('Стандарт Москва-Ташкент', 'Стандарт Москва-Ташкент'),
    ('Стандарт Ташкент-Москва', 'Стандарт Ташкент-Москва'),
    ('Ултрасрочный Москва-Ташкент', 'Ултрасрочный Москва-Ташкент'),
    ('Ултрасрочный Ташкент-Москва', 'Ултрасрочный Ташкент-Москва'),
    ('Духи Москва-Ташкент', 'Духи Москва-Ташкент'),
    ('Лекарство Москва-Ташкент', 'Лекарство Москва-Ташкент'),
)


# companyning balansini tuldirishlari istoriyasi
class CompanyAccountHistory(models.Model):
    uniq_id = models.CharField(max_length=50, default='00')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # customer_expenses = models.ForeignKey(CustomerExpensesHistory, on_delete=models.CASCADE,default='00')
    usd = models.FloatField(max_length=255, default='00')
    rub = models.FloatField(max_length=255, default='00')
    uzs = models.FloatField(max_length=255, default='00')
    currency_type = models.CharField(max_length=50, choices=CurrencyType, null=False, default=True)
    service_type = models.CharField(max_length=50, choices=ServiceType, default='00')
    plan_type = models.CharField(max_length=50, choices=PlanType, default='00')
    date_created = models.DateField(auto_now_add=True, blank=True)
    date_updated = models.DateField(auto_now=True, blank=True)

    def __str__(self):
        return str(self.user)


# companyning umumiy balans puli tepadagi tablisa yigindisi-summasi
class CompanyAccount(models.Model):
    # uniq_id = models.CharField(max_length=50, default=str(random.randint(1000,9999)))
    usd = models.FloatField(max_length=255, default='00')
    rub = models.FloatField(max_length=255, default='00')
    uzs = models.FloatField(max_length=255, default='00')
    date_created = models.DateField(auto_now_add=True, blank=True)
    date_updated = models.DateField(auto_now=True, blank=True)


# companydan ketgan pullar-harajatlar istoriyasi
class CompanyExpensesHistory(models.Model):
    uniq_id = models.CharField(max_length=50, default='00')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer_loan_history = models.ForeignKey(CustomerLoanHistory, on_delete=models.CASCADE, default='00')
    usd = models.FloatField(max_length=255, default='00')
    rub = models.FloatField(max_length=255, default='00')
    uzs = models.FloatField(max_length=255, default='00')
    currency_type = models.CharField(max_length=50, choices=CurrencyType, null=False, default=True)
    company_expenses_type = models.CharField(max_length=50, choices=CompanyExpensesType, default='00')
    date_created = models.DateField(auto_now_add=True, blank=True)
    date_updated = models.DateField(auto_now=True, blank=True)

    def __str__(self):
        return str(self.user)


# companydan ketgan pullar-harajatlar istoriyasi
class CompanyOwnExpensesHistory(models.Model):
    uniq_id = models.CharField(max_length=50, default='00')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    usd = models.FloatField(max_length=255, default='00')
    rub = models.FloatField(max_length=255, default='00')
    uzs = models.FloatField(max_length=255, default='00')
    currency_type = models.CharField(max_length=50, choices=CurrencyType, null=False, default=True)
    company_expenses_type = models.CharField(max_length=50, choices=CompanyExpensesType, default='00')
    date_created = models.DateField(auto_now_add=True, blank=True)
    date_updated = models.DateField(auto_now=True, blank=True)

    def __str__(self):
        return str(self.user)


# companyning umumiy harajati tepadagi janvalni yigindisi
class CompanyExpenses(models.Model):
    # uniq_id = models.CharField(max_length=50, default=str(random.randint(1000,9999)))
    usd = models.FloatField(max_length=255, default='00')
    rub = models.FloatField(max_length=255, default='00')
    uzs = models.FloatField(max_length=255, default='00')
    date_created = models.DateField(auto_now_add=True, blank=True)
    date_updated = models.DateField(auto_now=True, blank=True)

#
# # company bergan qarzlar istoriyasi
# class CompanyLoanHistory(models.Model):
#     uniq_id = models.CharField(max_length=50, default=str(random.sample(range(10000000), 1)))
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     customer_loan_history = models.ForeignKey(CustomerLoanHistory, on_delete=models.CASCADE)
#     usd = models.FloatField(max_length=255, default='00')
#     rub = models.FloatField(max_length=255, default='00')
#     uzs = models.FloatField(max_length=255, default='00')
#     currency_type = models.CharField(max_length=50, choices=CurrencyType, null=False, default=True)
#     general_status = models.CharField(max_length=50, choices=GeneralStatus, null=False, default=True)
#     loan_status = models.CharField(max_length=50, choices=LoanStatus, default='00')
#     date_created = models.DateField(auto_now_add=True, blank=True)
#     date_updated = models.DateField(auto_now=True, blank=True)
#
#     def __str__(self):
#         return str(self.user)
#
#
# # companyning umumiy qarzlari yigindisi
# class CompanyLoan(models.Model):
#     uniq_id = models.CharField(max_length=50, default=str(random.sample(range(10000000), 1)))
#     usd = models.FloatField(max_length=255, default='00')
#     rub = models.FloatField(max_length=255, default='00')
#     uzs = models.FloatField(max_length=255, default='00')
#     date_created = models.DateField(auto_now_add=True, blank=True)
#     date_updated = models.DateField(auto_now=True, blank=True)


