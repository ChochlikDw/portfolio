from django import forms
from .models import Expense
from django.contrib.auth.models import User

class ExpenseForm(forms.Form):
    pub_date = forms.DateField(label='Data', widget=forms.SelectDateWidget())
    price = forms.DecimalField(label='Cena', decimal_places=2)
    description = forms.CharField(label='Opis', max_length=200)

class LoginForm(forms.Form):
    username = forms.CharField(label='username', max_length=64)
    password = forms.CharField(label='password', widget=forms.PasswordInput())
