from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):

    username = forms.CharField(label="User")
    pwd = forms.CharField(label="Password", widget=forms.PasswordInput())


class SignUpForm(forms.Form):

    required_css_class = 'required'
    username = forms.RegexField(regex=r'^[0-9A-z]\w+$',
                                max_length=30,
                                label="Username",
                                error_messages={'invalid': "This value may contain only letters and numbers characters."})
    email = forms.EmailField(label="E-mail")
    password1 = forms.CharField(widget=forms.PasswordInput,
                                label="Password")
    password2 = forms.CharField(widget=forms.PasswordInput,
                                label="Password (again)")
    fist_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)

    def clean_username(self):
        username_existis = User.objects.filter(
            username=self.cleaned_data('username', ''))
        if username_existis.exists():
            raise forms.VAlidationError('A user with that name already exists')
        else:
            return self.cleaned_data('username')

    def clean_username(self):
        email_existis = User.objects.filter(
            email=self.cleaned_data('email', ''))
        if username_existis.exists():
            raise forms.VAlidationError('This email is already registered')
        else:
            return self.cleaned_data('email')

    def clean(self):
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError(
                    "The two password fields didn't match.")
        return self.cleaned_data
