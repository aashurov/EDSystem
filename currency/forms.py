from django import forms
from .models import *
from .forms import *


class CurrencyHistoryForm(forms.ModelForm):
    usd_rub = forms.FloatField(label='USD_RUB', required=False, widget=forms.NumberInput(attrs={"class": "form-control", "placeholder": "Доллар к рублю","required":"required"}))
    usd_uzs = forms.FloatField(label='USD_UZS', required=False, widget=forms.NumberInput(attrs={"class": "form-control", "placeholder": "Доллар к суму", "required":"required"}))

    class Meta:
        model = CurrencyHistory
        fields = ['usd_rub', 'usd_uzs']

