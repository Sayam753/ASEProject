from .models import Search
from django import forms

class SearchForm(forms.ModelForm):
    model=Search
    fields=['target','result']
