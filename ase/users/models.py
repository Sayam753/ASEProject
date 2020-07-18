from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

# Create your models here.

class UserProfile(AbstractUser):
    """
    User model has the details of the user.
    #Field Descriptions
    > username is a character field with value equal to the username of the user and is unique for every user
    > email field is the email id of the user
    > phone_no is a character field which stores the phone number of the user
    
    """
    username=models.CharField(max_length=25, blank=False, null=False, unique=True)
    email=models.EmailField(_('email address'), unique=True)
    subscribed = models.BooleanField(default=False)
    USERNAME_FIELD='username'
    REQUIRED_FIELDS=['email']

    def __str__(self):
        return f'{self.username}'
