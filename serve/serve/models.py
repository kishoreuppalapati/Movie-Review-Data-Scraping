from django.db import models

# Create your models here.
class Movie(models.Model):
    Id = models.IntegerField(primary_key=True)
    Name = models.TextField()
    YearNo = models.IntegerField()
    Awards = models.CharField(max_length = 25)

    class Meta:
        db_table = "Movie"