from django import forms
from .models import CustomerAccountHistory, CustomerAccount, CustomerLoanHistory, CustomerLoan
from django.contrib.auth.forms import SetPasswordForm, UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

CurrencyType = [
    ('USD', 'USD'),
    ('RUB', 'RUB'),
    ('UZS', 'UZS'),
]


class CustomerAccountHistoryForm(forms.ModelForm):
    usd = forms.FloatField(label='USD', required=False,
                          widget=forms.NumberInput(attrs={"class": "form-control", "placeholder": "USD", "id": "parcelPriceUS", "onkeyup": "priceCustomUS()", "required":"required"}))
    rub = forms.FloatField(label='RUB', required=False,
                          widget=forms.NumberInput(attrs={"class": "form-control", "placeholder": "RUB", "id": "parcelPriceRU", "onkeyup": "priceCustomRU()", "required":"required"}))
    uzs = forms.FloatField(label='UZS', required=False,
                          widget=forms.NumberInput(attrs={"class": "form-control", "placeholder": "UZS", "id": "parcelPriceUZS", "onkeyup": "priceCustomUZS()", "required":"required"}))
    currency_type = forms.ChoiceField(label='CurrencyType', widget=forms.Select(attrs={"class": "form-control"}), choices=CurrencyType)

    class Meta:
        model = CustomerAccountHistory
        fields = ['usd', 'rub', 'uzs', 'currency_type']


class CustomerAccountForm(forms.ModelForm):
    usd = forms.FloatField(label='USD', required=False,
                          widget=forms.NumberInput(attrs={"class": "form-control", "placeholder": "USD", "id": "parcelPriceUS", "onkeyup": "priceCustomUS()", "required":"required"}))
    rub = forms.FloatField(label='RUB', required=False,
                          widget=forms.NumberInput(attrs={"class": "form-control", "placeholder": "RUB", "id": "parcelPriceRU", "onkeyup": "priceCustomRU()", "required":"required"}))
    uzs = forms.FloatField(label='UZS', required=False,
                          widget=forms.NumberInput(attrs={"class": "form-control", "placeholder": "UZS", "id": "parcelPriceUZS", "onkeyup": "priceCustomUZS()", "required":"required"}))

    class Meta:
        model = CustomerAccount
        fields = ['usd', 'rub', 'uzs']


class CustomerLoanHistoryForm(forms.ModelForm):
    usd = forms.FloatField(label='USD', required=False,
                          widget=forms.NumberInput(attrs={"class": "form-control", "placeholder": "USD", "id": "parcelPriceUS", "onkeyup": "priceCustomUS()", "required":"required"}))
    rub = forms.FloatField(label='RUB', required=False,
                          widget=forms.NumberInput(attrs={"class": "form-control", "placeholder": "RUB", "id": "parcelPriceRU", "onkeyup": "priceCustomRU()", "required":"required"}))
    uzs = forms.FloatField(label='UZS', required=False,
                          widget=forms.NumberInput(attrs={"class": "form-control", "placeholder": "UZS", "id": "parcelPriceUZS", "onkeyup": "priceCustomUZS()", "required":"required"}))
    currency_type = forms.ChoiceField(label='CurrencyType', widget=forms.Select(attrs={"class": "form-control"}), choices=CurrencyType)

    class Meta:
        model = CustomerLoanHistory
        fields = ['usd', 'rub', 'uzs', 'currency_type']


class CustomerLoanForm(forms.ModelForm):
    usd = forms.FloatField(label='USD', required=False,
                          widget=forms.NumberInput(attrs={"class": "form-control", "placeholder": "USD", "id": "parcelPriceUS", "onkeyup": "priceCustomUS()", "required":"required"}))
    rub = forms.FloatField(label='RUB', required=False,
                          widget=forms.NumberInput(attrs={"class": "form-control", "placeholder": "RUB", "id": "parcelPriceRU", "onkeyup": "priceCustomRU()", "required":"required"}))
    uzs = forms.FloatField(label='UZS', required=False,
                          widget=forms.NumberInput(attrs={"class": "form-control", "placeholder": "UZS", "id": "parcelPriceUZS", "onkeyup": "priceCustomUZS()", "required":"required"}))
    currency_type = forms.ChoiceField(label='CurrencyType', widget=forms.Select(attrs={"class": "form-control"}), choices=CurrencyType)

    class Meta:
        model = CustomerLoanHistory
        fields = ['usd', 'rub', 'uzs', 'currency_type']