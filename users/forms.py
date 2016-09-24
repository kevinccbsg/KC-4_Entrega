from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm


class LoginForm(forms.Form):

    username = forms.CharField(label="User")
    pwd = forms.CharField(label="Password", widget=forms.PasswordInput())


class SignUpForm(ModelForm):

    class Meta:
        model = User
        fields = ('username', 'password', 'first_name', 'last_name', 'email',)
