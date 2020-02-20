from django.db import models

# Create your models here.
class Search(models.Model):
    target=models.CharField(max_length=50)
    result=models.TextField()
