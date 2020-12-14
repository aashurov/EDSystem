from django import forms
from company.models import *


class CompanyAccountHistoryForm(forms.ModelForm):
    usd = forms.FloatField(label='USD', required=False, widget=forms.NumberInput(attrs={"class": "form-control", "placeholder":"USD", "id": "parcelPriceUS", "onkeyup": "priceCustomUS()"}))
    plan_type = forms.ChoiceField(label='PlanType', widget=forms.Select, choices=PlanType)
    service_type = forms.ChoiceField(label='ServiceType', widget=forms.Select, choices=ServiceType)

    class Meta:
        model = CompanyAccountHistory
        fields = ['usd', 'plan_type', 'service_type']


class CompanyExpensesHistoryForm(forms.ModelForm):
    usd = forms.FloatField(label='USD', required=False, widget=forms.NumberInput(attrs={"class": "form-control", "placeholder":"USD", "id": "parcelPriceUS", "onkeyup": "priceCustomUS()"}))
    company_expenses_type = forms.ChoiceField(label='PlanType', widget=forms.Select(attrs={"class": "form-control"}), choices=CompanyExpensesType)

    class Meta:
        model = CompanyExpensesHistory
        fields = ['usd', 'company_expenses_type']


class CompanyOwnExpensesHistoryForm(forms.ModelForm):
    usd = forms.FloatField(label='USD', required=False, widget=forms.NumberInput(attrs={"class": "form-control", "placeholder":"USD", "id": "parcelPriceUS", "onkeyup": "priceCustomUS()"}))
    company_expenses_type = forms.ChoiceField(label='PlanType', widget=forms.Select(attrs={"class": "form-control"}), choices=CompanyExpensesType)

    class Meta:
        model = CompanyOwnExpensesHistory
        fields = ['usd', 'company_expenses_type']