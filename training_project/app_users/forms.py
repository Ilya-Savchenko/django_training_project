from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import UsersModel


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(help_text='Имя')
    last_name = forms.CharField(help_text='Фамилия')
    phone_number = forms.CharField(help_text='Номер телефона')
    city = forms.CharField(help_text='Город проживания')

    class Meta:
        model = User
        fields = (
            'username',
            'password1',
            'password2',
            'email',
            'first_name',
            'last_name',
            'phone_number',
            'city',
        )
