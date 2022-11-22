from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

REGIONS = (
    ('NA', 'North America'),
    ('SA', 'South America'),
    ('CA', 'Central America'),
    ('EU', 'Europe'),
    ('AS', 'Asia'),
    ('ME', 'Middle East'),
    ('AF', 'Africa'),
    ('OC', 'Oceania'),
)

# Create your models here.

class Recipe(models.Model):
    name = models.CharField(max_length=200)
    ingredients = models.CharField(max_length=2000)
    directions = models.TextField(max_length=2000)
    description = models.TextField(max_length=500)
    region = models.CharField(
        max_length=2,
        choices=REGIONS,
        default=REGIONS[0][0]
    )
    # user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} ({self.id})'