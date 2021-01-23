from django import forms
from .models import *


class ParcelMainForm(forms.ModelForm):
    parcel_plan = forms.CharField(widget=forms.NumberInput(attrs={"onkeyup":"calculate();", "name":"parcel_plan", "onchange":"calculate();", "id": "standard3", "class": "form-control", "placeholder": "Выберите тариф" }))
    parcel_length = forms.FloatField(widget=forms.NumberInput(attrs={"onkeyup":"calculate();", "name":"parcel_length", "onchange":"calculate();", "id": "parcel_length", "class": "form-control", "placeholder": "Длина" }))
    parcel_width = forms.FloatField(widget=forms.NumberInput(attrs={"onkeyup":"calculate();", "name":"parcel_width", "onchange":"calculate();","id": "parcel_width", "class": "form-control", "placeholder": "Ширина" }))
    parcel_height = forms.FloatField(widget=forms.NumberInput(attrs={"onkeyup":"calculate();", "name":"parcel_height", "onchange":"calculate();", "id": "parcel_height", "class": "form-control", "placeholder": "Высота" }))
    parcel_dimension = forms.FloatField(widget=forms.NumberInput(attrs={"onkeyup":"calculate();", "name":"parcel_dimension", "onchange":"calculate();", "id": "parcel_dimension", "class": "form-control", "placeholder": "Габарит", "readonly":"readonly"}))
    parcel_weight = forms.FloatField(widget=forms.NumberInput(attrs={"onkeyup":"calculate();", "name":"parcel_weight", "onchange":"calculate();", "id": "parcel_weight", "class": "form-control", "placeholder": "Вес" }))
    parcel_cost = forms.FloatField(widget=forms.NumberInput(attrs={"id": "cost", "class": "form-control","name":"parcel_cost", "id": "parcel_cost", "placeholder": "Цена", "required":"required"}))

    class Meta:
        model = ParcelMain
        fields = [ 'parcel_length', 'parcel_width', 'parcel_height', 'parcel_dimension', 'parcel_weight', 'parcel_cost']

