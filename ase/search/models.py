from django.db import models


# Create your models here.
class Search(models.Model):
    """
	Search model has query details.
	#Field Description
	> query is a character field which keeps track of all the queries made onsite

	"""
    query = models.CharField(max_length=100)

    def __repr__(self):
        return f"{self.query}"
