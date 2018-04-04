from django.contrib.auth.models import User
from django import forms
from .models import ContractModel


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class CreateContractForm(forms.ModelForm):

    class Meta:
        model = ContractModel
        fields = ['name']
