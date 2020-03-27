from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
# from django.conf import settings

# Create your models here.

class user(AbstractUser):
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
