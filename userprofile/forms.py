from django import forms
from .models import UserProfile
from django.contrib.auth.forms import SetPasswordForm, UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm


class UserForm(UserCreationForm):
    first_name = forms.CharField()
    last_name = forms.CharField()

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None


class SetpasswordLogin(SetPasswordForm):
    new_password1 = forms.CharField(label='Новый пароль', widget=forms.PasswordInput(attrs={"class": "form-control"}))
    new_password2 = forms.CharField(label='Потверждение', widget=forms.PasswordInput(attrs={"class": "form-control"}))


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder": "Username"}))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Password"}))


class UserUpdateForm(forms.ModelForm):
    username = forms.CharField(label='Пользователь', required=True, max_length=30,
                               widget=forms.TextInput(attrs={"class": "form-control"}))
    email = forms.EmailField(required=False, max_length=75, widget=forms.TextInput(attrs={"class": "form-control"}))
    first_name = forms.CharField(label='Имя', required=False, max_length=255,
                                 widget=forms.TextInput(attrs={"class": "form-control"}))
    last_name = forms.CharField(label='Иsмя', required=False, max_length=255,
                                widget=forms.TextInput(attrs={"class": "form-control"}))

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']


class ProfileUpdateForm(forms.ModelForm):
    uniq_id = forms.CharField(label='ID пользователя', required=False, max_length=30,
                              widget=forms.TextInput(attrs={"class": "form-control", "readonly": "readonly"}))
    phone_number = forms.CharField(label='Номер телефона', required=False, max_length=255,
                                   widget=forms.TextInput(attrs={"class": "form-control", "id": "phone"}))
    address_first = forms.CharField(label='Адрес доставки', required=False, max_length=255,
                                    widget=forms.TextInput(attrs={"class": "form-control"}))
    address_second = forms.CharField(label='Адрес доставки', required=False, max_length=255,
                                     widget=forms.TextInput(attrs={"class": "form-control"}))
    passport_number = forms.CharField(label='Серия паспорта', required=False, max_length=255,
                                      widget=forms.TextInput(attrs={"class": "form-control", "id": "passport_number"}))
    passport_date_first = forms.DateField(label='Дата выдачи', required=False, widget=forms.DateInput(
        attrs={'class': 'form-control datepicker', "id": "passport_date_first"}))
    passport_date_second = forms.DateField(label='Срок', required=False, widget=forms.DateInput(
        attrs={'class': 'form-control', "id": "passport_date_second"}))
    passport_organization = forms.CharField(label='Кем Выдан', required=False, max_length=255,
                                            widget=forms.TextInput(attrs={"class": "form-control"}))
    user_organization = forms.CharField(label='Организация', required=False, max_length=255,
                                        widget=forms.TextInput(attrs={"class": "form-control"}))
    description = forms.CharField(label='Коментарии', required=False, max_length=255,
                                  widget=forms.TextInput(attrs={"class": "form-control"}))
    avatar_image = forms.ImageField()
    passport_image = forms.ImageField()
    passport_image_behind = forms.ImageField()

    class Meta:
        model = UserProfile
        fields = ['uniq_id', 'phone_number', 'address_first', 'address_second', 'passport_number',
                  'passport_date_first', 'passport_date_second', 'passport_organization', 'user_organization',
                  'avatar_image', 'passport_image', 'passport_image_behind']
#
#
# class SetpasswordLogin(SetPasswordForm):
#     new_password1 = forms.CharField(label='Новый пароль', widget=forms.PasswordInput(attrs={"class": "form-control"}))
#     new_password2 = forms.CharField(label='Потверждение', widget=forms.PasswordInput(attrs={"class": "form-control"}))