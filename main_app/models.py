from django.db import models

# Create your models here.
# define plant model here
class Plant(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    size = models.IntegerField()
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.name