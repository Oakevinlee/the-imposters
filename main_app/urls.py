from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('recipe/', views.recipes_index, name='index'),
    path('recipes/<int:recipe_id>/', views.recipes_detail, name='detail'),
    path('accounts/signup/', views.signup, name='signup'),
    path('recipes/create/', views.RecipeCreate.as_view(), name='recipes_create'),
]