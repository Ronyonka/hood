from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from .models import *

class SignUpForm(UserCreationForm):
    '''
    Form that extends the UserCreationForm
    Added fields are the email fields
    '''
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    email= forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email'}), max_length=64)
    password1= forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}))


    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields + ("email","username","password1")
