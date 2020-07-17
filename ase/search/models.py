from django.db import models


# Create your models here.
class Search(models.Model):
    """
    -- Summary --
    Search model has query details.
    #Field Description
    > query is a character filed with max possible length = 100, which is basically the user query.

    """
    query = models.CharField(max_length=100)

    def __repr__(self):
        return f"{self.query}"
