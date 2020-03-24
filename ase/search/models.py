from django.db import models


# Create your models here.
class Search(models.Model):
    query = models.CharField(max_length=100)

    def __repr__(self):
        return f"{self.query}"
