from django.contrib import admin
from .models import Recipe, Review, Photo

# Register your models here.
admin.site.register(Recipe)
admin.site.register(Review)
admin.site.register(Photo)