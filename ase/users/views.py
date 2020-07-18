from django.shortcuts import render, redirect

from users.models import UserProfile
from users import forms


# Create your views here.
def register(request):
    """
    register view returns the user registration form

    """
    if request.method == "POST":
        form = forms.UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            # messages.success(request,f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = forms.UserRegistrationForm()

    return render(request,'users/register.html', {'form':form})
