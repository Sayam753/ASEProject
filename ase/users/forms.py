from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import user

class UserRegistrationForm(UserCreationForm):
    # email=forms.EmailField()
    password1=forms.CharField(widget=forms.PasswordInput(attrs={'id':'pass','class':'input'}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'id':'pass','class':'input'}))

    class Meta:
        model=user
        fields=['username','email','first_name','password1','password2']
        widgets={
        'username':forms.TextInput(attrs={'id':'user', 'class':'input'}),
        'email':forms.EmailInput(attrs={'id':'user', 'class':'input'}),
        'first_name':forms.TextInput(attrs={'id':'user', 'class':'input'}),
        }
