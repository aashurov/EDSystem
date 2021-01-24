from customer.models import *
# Create your models here.

GeneralStatus = (
    ('В обработке', 'В обработке'),
    ('Одобрено', 'Одобрено'),
)

LoanStatus = (
    ('Занял', 'Занял'),
    ('Вернул', 'Вернул'),
)


ServiceType = (
    ('За Товар', 'За Товар'),
    ('За перевозку Москва-Ташкент', 'За перевозку Москва-Ташкент'),
    ('За перевозку Ташкент-Москва', 'За перевозку Ташкент-Москва'),
    ('Вернуть клиенту', 'Вернуть клиенту'),

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
    usd = models.FloatField(max_length=255, default='00')
    staff_id = models.CharField(max_length=50, default='00')
    service_type = models.CharField(max_length=50, choices=ServiceType, default='00')
    description = models.CharField(max_length=255, default='00')
    plan_type = models.CharField(max_length=50, choices=PlanType, default='00')
    date_created = models.DateField(auto_now_add=True, blank=True)
    date_updated = models.DateField(auto_now=True, blank=True)

    def __str__(self):
        return str(self.user)


# companyning umumiy balans puli tepadagi tablisa yigindisi-summasi
class CompanyAccount(models.Model):
    usd = models.FloatField(max_length=255, default='00')
    date_created = models.DateField(auto_now_add=True, blank=True)
    date_updated = models.DateField(auto_now=True, blank=True)


# companydan ketgan pullar-harajatlar istoriyasi
class CompanyExpensesHistory(models.Model):
    uniq_id = models.CharField(max_length=50, default='00')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer_loan_history = models.ForeignKey(CustomerLoanHistory, on_delete=models.CASCADE, default='00')
    usd = models.FloatField(max_length=255, default='00')
    staff_id = models.CharField(max_length=50, default='00')
    company_expenses_type = models.CharField(max_length=50, choices=CompanyExpensesType, default='00')
    description = models.CharField(max_length=255, default='00')
    date_created = models.DateField(auto_now_add=True, blank=True)
    date_updated = models.DateField(auto_now=True, blank=True)

    def __str__(self):
        return str(self.user)


# companydan ketgan pullar-harajatlar istoriyasi
class CompanyOwnExpensesHistory(models.Model):
    uniq_id = models.CharField(max_length=50, default='00')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    usd = models.FloatField(max_length=255, default='00')
    staff_id = models.CharField(max_length=50, default='00')
    company_expenses_type = models.CharField(max_length=50, choices=CompanyExpensesType, default='00')
    description = models.CharField(max_length=255, default='00')
    date_created = models.DateField(auto_now_add=True, blank=True)
    date_updated = models.DateField(auto_now=True, blank=True)

    def __str__(self):
        return str(self.user)


# companyning umumiy harajati tepadagi janvalni yigindisi
class CompanyExpenses(models.Model):
    usd = models.FloatField(max_length=255, default='00')
    date_created = models.DateField(auto_now_add=True, blank=True)
    date_updated = models.DateField(auto_now=True, blank=True)
