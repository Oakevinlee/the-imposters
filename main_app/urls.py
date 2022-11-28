from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('recipe/', views.recipes_index, name='index'),
    path('recipes/<int:recipe_id>/', views.recipes_detail, name='detail'),
    path('accounts/signup/', views.signup, name='signup'),
    path('recipes/create/', views.RecipeCreate.as_view(), name='recipes_create'),
    path('recipes/<int:pk>/update/', views.RecipeUpdate.as_view(), name='recipes_update'),
    path('recipes/<int:pk>/delete/', views.RecipeDelete.as_view(), name='recipes_delete'),
    path('recipes/<int:recipe_id>/add_review/', views.add_review, name='add_review'),
    path('recipes/<int:pk>/delete_review/', views.ReviewDelete.as_view(), name='delete_review'),
    path('search/', views.SearchResultsView.as_view(), name="search_results"),
]