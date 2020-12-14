from django import forms
from .models import CustomerAccountHistory, CustomerAccount, CustomerLoanHistory

CurrencyType = [
    ('USD', 'USD'),
    ('RUB', 'RUB'),
    ('UZS', 'UZS'),
]


class CustomerAccountHistoryForm(forms.ModelForm):
    usd = forms.FloatField(label='USD', required=False, widget=forms.NumberInput(attrs={"class": "form-control", "placeholder": "USD", "id": "parcelPriceUS", "onkeyup": "priceCustomUS()", "required":"required"}))
    class Meta:
        model = CustomerAccountHistory
        fields = ['usd']


class CustomerAccountForm(forms.ModelForm):
    usd = forms.FloatField(label='USD', required=False, widget=forms.NumberInput(attrs={"class": "form-control", "placeholder": "USD", "id": "parcelPriceUS", "onkeyup": "priceCustomUS()", "required":"required"}))

    class Meta:
        model = CustomerAccount
        fields = ['usd']


class CustomerLoanHistoryForm(forms.ModelForm):
    usd = forms.FloatField(label='USD', required=False, widget=forms.NumberInput(attrs={"class": "form-control", "placeholder": "USD", "id": "parcelPriceUS", "onkeyup": "priceCustomUS()", "required":"required"}))

    class Meta:
        model = CustomerLoanHistory
        fields = ['usd']


class CustomerLoanForm(forms.ModelForm):
    usd = forms.FloatField(label='USD', required=False, widget=forms.NumberInput(attrs={"class": "form-control", "placeholder": "USD", "id": "parcelPriceUS", "onkeyup": "priceCustomUS()", "required":"required"}))

    class Meta:
        model = CustomerLoanHistory
        fields = ['usd']