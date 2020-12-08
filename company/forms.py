from django import forms
from django.forms import ModelChoiceField
from customer.models import CustomerAccount, CustomerLoan
from django.contrib.auth.models import User
from main.models import *
from company.models import *


class CompanyAccountHistoryForm(forms.ModelForm):
    usd = forms.FloatField(label='USD', required=False,
                          widget=forms.NumberInput(attrs={"class": "form-control", "id": "parcelPriceUS", "onkeyup": "priceCustomUS()"}))
    rub = forms.FloatField(label='RUB', required=False,
                          widget=forms.NumberInput(attrs={"class": "form-control", "id": "parcelPriceRU", "onkeyup": "priceCustomRU()"}))
    uzs = forms.FloatField(label='UZS', required=False,
                          widget=forms.NumberInput(attrs={"class": "form-control", "id": "parcelPriceUZS", "onkeyup": "priceCustomUZS()"}))
    currency_type = forms.ChoiceField(label='CurrencyType', widget=forms.Select, choices=CurrencyType)
    plan_type = forms.ChoiceField(label='PlanType', widget=forms.Select, choices=PlanType)
    service_type = forms.ChoiceField(label='ServiceType', widget=forms.Select, choices=ServiceType)

    class Meta:
        model = CompanyAccountHistory
        fields = ['usd', 'rub', 'uzs', 'currency_type', 'plan_type', 'service_type']


class CompanyExpensesHistoryForm(forms.ModelForm):
    usd = forms.FloatField(label='USD', required=False,
                          widget=forms.NumberInput(attrs={"class": "form-control", "id": "parcelPriceUS", "onkeyup": "priceCustomUS()"}))
    rub = forms.FloatField(label='RUB', required=False,
                          widget=forms.NumberInput(attrs={"class": "form-control", "id": "parcelPriceRU", "onkeyup": "priceCustomRU()"}))
    uzs = forms.FloatField(label='UZS', required=False,
                          widget=forms.NumberInput(attrs={"class": "form-control", "id": "parcelPriceUZS", "onkeyup": "priceCustomUZS()"}))
    currency_type = forms.ChoiceField(label='CurrencyType', widget=forms.Select, choices=CurrencyType)
    company_expenses_type = forms.ChoiceField(label='PlanType', widget=forms.Select, choices=CompanyExpensesType)

    class Meta:
        model = CompanyExpensesHistory
        fields = ['usd', 'rub', 'uzs', 'currency_type', 'company_expenses_type']


class CompanyOwnExpensesHistoryForm(forms.ModelForm):
    usd = forms.FloatField(label='USD', required=False,
                          widget=forms.NumberInput(attrs={"class": "form-control", "id": "parcelPriceUS", "onkeyup": "priceCustomUS()"}))
    rub = forms.FloatField(label='RUB', required=False,
                          widget=forms.NumberInput(attrs={"class": "form-control", "id": "parcelPriceRU", "onkeyup": "priceCustomRU()"}))
    uzs = forms.FloatField(label='UZS', required=False,
                          widget=forms.NumberInput(attrs={"class": "form-control", "id": "parcelPriceUZS", "onkeyup": "priceCustomUZS()"}))
    currency_type = forms.ChoiceField(label='CurrencyType', widget=forms.Select, choices=CurrencyType)
    company_expenses_type = forms.ChoiceField(label='PlanType', widget=forms.Select, choices=CompanyExpensesType)

    class Meta:
        model = CompanyOwnExpensesHistory
        fields = ['usd', 'rub', 'uzs', 'currency_type', 'company_expenses_type']