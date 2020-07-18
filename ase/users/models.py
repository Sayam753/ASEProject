from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
# from django.conf import settings

# Create your models here.

class user(AbstractUser):
    """
    User model has the details of the user.
    #Field Descriptions
    > username is a character field with value equal to the username of the user and is unique for every user
    > email field is the email id of the user
    > phone_no is a character field which stores the phone number of the user
    
    """
    username=models.CharField(max_length=25, blank=False, null=False, unique=True)
    email=models.EmailField(_('email address'), unique=True)
    # first_name=models.CharField(max_length=30,blank=False, null=False)
    # middle_name=models.CharField(blank=True, null=True)
    # last_name=models.CharField(blank=False, null=False)
    phone_no=models.CharField(max_length=10, blank=True, null=True, unique=True)
    # password=models.CharField(max_length=20, blank=False, null=False)
    # confirm_password=models.CharField(max_length=20, blank=False, null=False)
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['username','name', 'password','confirm_password']

    def __str__(self):
        return f'{self.email}'
