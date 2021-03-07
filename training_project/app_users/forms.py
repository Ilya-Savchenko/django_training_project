from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(help_text='Имя')
    last_name = forms.CharField(help_text='Фамилия')
    email = forms.EmailField(widget=forms.EmailInput)
    day_of_birth = forms.DateField(widget=forms.DateInput, help_text='Дата рождения (ДД/ММ/ГГГГ)')
    card_number = forms.CharField(help_text='Номер скидочной карты')
    phone_number = forms.CharField(help_text='Номер телефона')
    city = forms.CharField(help_text='Город проживания')

    class Meta:
        model = User
        fields = (
        'username',
        'first_name',
        'last_name',
        'email',
        'city',
        'day_of_birth',
        'phone_number',
        'card_number',
        'password1',
        'password2'
        )
