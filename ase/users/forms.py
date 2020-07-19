from django import forms
from django.contrib.auth.forms import UserCreationForm

from users.models import UserProfile

class UserRegistrationForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'id':'pass','class':'input'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'id':'pass','class':'input'}))

    class Meta:
        model=UserProfile
        fields=['email','username','password1','password2']
        widgets={
        'username':forms.TextInput(attrs={'id':'user', 'class':'input'}),
        'email':forms.EmailInput(attrs={'id':'user', 'class':'input'}),
        }
