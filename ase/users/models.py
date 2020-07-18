from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

# Create your models here.

class UserProfile(AbstractUser):
    username=models.CharField(max_length=25, blank=False, null=False, unique=True)
    email=models.EmailField(_('email address'), unique=True)
    subscribed = models.BooleanField(default=False)
    USERNAME_FIELD='username'
    REQUIRED_FIELDS=['email']

    def __str__(self):
        return f'{self.username}'
