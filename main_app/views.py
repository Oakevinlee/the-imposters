from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Recipe, Review
from .forms import ReviewForm
from django.db.models import Q

# Create your views here.
def home(request):
    return render(request, 'home.html')
    
def about(request):
    return render(request, 'about.html')
    
def recipes_index(request):
  recipes = Recipe.objects.all()
  return render(request, 'recipes/index.html', {
    'recipes': recipes
})

def recipes_detail(request, recipe_id):
  recipe = Recipe.objects.get(id=recipe_id)
  review_form = ReviewForm()
  return render(request, 'recipes/detail.html', {
    'recipe': recipe, 'review_form': review_form
  })

class RecipeCreate(LoginRequiredMixin, CreateView):
  model = Recipe
  fields = ['name', 'ingredients', 'description', 'directions','region']
  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class RecipeUpdate(LoginRequiredMixin, UpdateView):
    model = Recipe
    fields = ['name', 'ingredients', 'description', 'directions','region']

class RecipeDelete(LoginRequiredMixin, DeleteView):
    model = Recipe
    success_url  = '/recipe'

@login_required
def add_review(request, recipe_id):
  form = ReviewForm(request.POST)
  if form.is_valid():
    new_review = form.save(commit=False)
    new_review.recipe_id = recipe_id
    new_review.user = request.user
    new_review.save()
  return redirect('detail', recipe_id=recipe_id)

class ReviewDelete(LoginRequiredMixin, DeleteView):
  model = Review
  success_url = '/recipe'

class SearchResultsView(ListView):
  model = Recipe

  def get_queryset(self):
    query = self.request.GET.get("q")
    object_list = Recipe.objects.filter(
      Q(name__icontains=query) | Q(region__icontains=query)
    )
    return object_list

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)