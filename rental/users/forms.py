from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from .models import User

class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(label="Имя", max_length=50)
    last_name = forms.CharField(label="Фамилия", max_length=50)
    middle_name = forms.CharField(label="Отчество (опционально)", max_length=50, required=False)
    city = forms.CharField(label="Город проживания", max_length=100)
    email = forms.EmailField(label="Адрес электронной почты")
    phone_number = forms.CharField(label="Номер телефона", max_length=15)
    role = forms.ChoiceField(choices=User.ROLE_CHOICES, label="Выберите роль")

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'middle_name', 'city', 'phone_number', 'role', 'password1', 'password2']

class UserLoginForm(AuthenticationForm):
    username = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={'class': 'form-control'}))