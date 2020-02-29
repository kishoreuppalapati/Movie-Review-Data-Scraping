from django.db import models


# Create your models here.
class Movie(models.Model):
    #id = models.IntegerField()
    name = models.TextField()
    year = models.IntegerField()
    awarad = models.CharField(max_length = 25)

    def __str__(self):
        return self.name