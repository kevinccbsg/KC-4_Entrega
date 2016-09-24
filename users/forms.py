from django import forms
from django.forms import ModelForm

class LoginForm(forms.Form):

    username = forms.CharField(label="User")
    pwd = forms.CharField(label="Password", widget=forms.PasswordInput())

#class SignUpForm(ModelForm):
#
#	'''
#    Form to create a Post
#    '''
#    class Meta:
#        model = Post
#        flields = ('',)

