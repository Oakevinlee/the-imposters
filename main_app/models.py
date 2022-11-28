from django.db import models
from django.urls import reverse
from datetime import datetime
from django.contrib.auth.models import User

REGIONS = (
    ('NORTH AMERICAN', 'North America'),
    ('SOUTH AMERICAN', 'South America'),
    ('CENTRAL AMERICAN', 'Central America'),
    ('EUROPEAN', 'Europe'),
    ('ASIAN', 'Asia'),
    ('MIDDLE EASTERN', 'Middle East'),
    ('AFRICAN', 'Africa'),
    ('OCEANIC', 'Oceania'),
)

RATINGS = (
    ('EX', 'Excellent!'),
    ('YM', 'Yummy!'),
    ('AL', 'Alright.'),
    ('MH', 'Meh...'),
    ('DS', 'Disgusting.'),
)

# Create your models here.

class Recipe(models.Model):
    name = models.CharField(max_length=200)
    ingredients = models.TextField(max_length=2000)
    directions = models.TextField(max_length=2000)
    description = models.TextField(max_length=500)
    region = models.CharField(
        max_length=16,
        choices=REGIONS,
        default=REGIONS[0][0]
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} ({self.id})'

    def get_absolute_url(self):
        return reverse('detail', kwargs={'recipe_id': self.id})

class Review(models.Model):
    comment = models.TextField(max_length=300)
    date = models.DateTimeField(default=datetime.now)
    rating = models.CharField(
        max_length=2,
        choices=RATINGS,
        default=RATINGS[0][0]
    )



    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.comment} has a rating of {self.rating}."

    class Meta:
        ordering = ['-date']

class Photo(models.Model):
  url = models.CharField(max_length=200)
  recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

  def __str__(self):
    return f"Photo for recipe_id: {self.recipe_id} @{self.url}"