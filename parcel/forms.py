from django import forms
from .models import *


class ParcelMainForm(forms.ModelForm):
    sender_id = forms.CharField(widget=forms.NumberInput(attrs={"onkeyup":"calculate();", "onchange":"calculate();", "id": "standard1", "class": "form-control", "placeholder": "Выберите отправителя" }))
    recipient_id = forms.CharField(widget=forms.NumberInput(attrs={"id": "standard2", "class": "form-control", "placeholder": "Выберите получателя" }))
    parcel_plan = forms.CharField(widget=forms.NumberInput(attrs={"onkeyup":"calculate();", "onchange":"calculate();", "id": "1standard3", "class": "form-control", "placeholder": "Выберите тариф" }))
    parcel_zabor = forms.BooleanField(label='Забор посылки', widget=forms.CheckboxInput(attrs={"onkeyup":"calculate();",   "onchange":"calculate();", "id": "parcel_zabor", "class": "form-control", "placeholder": "Забор посылки" }))
    parcel_dostavka = forms.BooleanField(label='Доставка посылки', widget=forms.CheckboxInput(attrs={"onkeyup":"calculate();", "onchange":"calculate();", "id": "parcel_dostavka", "class": "form-control", "placeholder": "Доставка посылки" }))
    parcel_length = forms.FloatField(widget=forms.NumberInput(attrs={"onkeyup":"calculate();", "onchange":"calculate();", "id": "parcel_length", "class": "form-control", "placeholder": "Длина" }))
    parcel_width = forms.FloatField(widget=forms.NumberInput(attrs={"onkeyup":"calculate();", "onchange":"calculate();","id": "parcel_width", "class": "form-control", "placeholder": "Ширина" }))
    parcel_height = forms.FloatField(widget=forms.NumberInput(attrs={"onkeyup":"calculate();", "onchange":"calculate();", "id": "parcel_height", "class": "form-control", "placeholder": "Высота" }))
    parcel_dimension = forms.FloatField(widget=forms.NumberInput(attrs={"onkeyup":"calculate();", "onchange":"calculate();", "id": "parcel_dimension", "class": "form-control", "placeholder": "Габарит"}))
    parcel_weight = forms.FloatField(widget=forms.NumberInput(attrs={"onkeyup":"calculate();", "onchange":"calculate();", "id": "parcel_weight", "class": "form-control", "placeholder": "Вес" }))
    parcel_cost = forms.FloatField(widget=forms.NumberInput(attrs={"class": "form-control", "id": "parcel_cost", "placeholder": "Цена", "required":"required"}))

    class Meta:
        model = ParcelMain
        fields = ['sender_id','recipient_id', 'parcel_plan', 'parcel_zabor', 'parcel_dostavka', 'parcel_length', 'parcel_width', 'parcel_height', 'parcel_dimension', 'parcel_weight', 'parcel_cost']

class ParcelItemsForm(forms.ModelForm):
    prod_url = forms.CharField(widget=forms.NumberInput(attrs={"onkeyup":"calculate();", "onchange":"calculate();", "id": "1standard1", "class": "form-control", "placeholder": "Выберите отправителя" }))
    prod_name = forms.CharField(widget=forms.NumberInput(attrs={"onkeyup":"calculate();", "onchange":"calculate();", "id": "1standard2", "class": "form-control", "placeholder": "Выберите получателя" }))
    prod_cnt = forms.CharField(widget=forms.NumberInput(attrs={"onkeyup":"calculate();", "onchange":"calculate();", "id": "1standard3", "class": "form-control", "placeholder": "Выберите тариф" }))
    prod_cost = forms.BooleanField(label='Забор посылки', widget=forms.CheckboxInput(attrs={"onkeyup":"calculate();",   "onchange":"calculate();", "id": "parcel_zabor", "class": "form-control", "placeholder": "Забор посылки" }))
    prod_tnved = forms.BooleanField(label='Доставка посылки', widget=forms.CheckboxInput(attrs={"onkeyup":"calculate();", "onchange":"calculate();", "id": "parcel_dostavka", "class": "form-control", "placeholder": "Доставка посылки" }))

    class Meta:
        model = ParcelItems
        fields = ['prod_url','prod_name', 'prod_cnt', 'prod_cost', 'prod_tnved']
