from django.db import models
from django.urls import reverse

WATER = (
    ('I','infrequent'),
    ('R','regular'),
    ('F','frequent')
)
class Soil(models.Model):
    soil_type = models.CharField(max_length=50)
    benefit = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('soils_detail', kwargs={'pk': self.id})


class Plant(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    size = models.IntegerField()
    category = models.CharField(max_length=100)
    soils = models.ManyToManyField(Soil)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'plant_id': self.id})
    
    
class Feeding(models.Model):
    water_needs = models.CharField('Watering Needs',
    max_length =1,
    choices= WATER,
    default=WATER[0][0])

    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_water_needs_display()}"