from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Recipe

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
  # First, create a list of the toy ids that the cat DOES have

  # id_list = cat.toys.all().values_list('id')

  # Query for the toys that the cat doesn't have
  # by using the exclude() method vs. the filter() method
  # toys_cat_doesnt_have = Toy.objects.exclude(id__in=id_list)
  # instantiate FeedingForm to be rendered in detail.html
  # feeding_form = FeedingForm()
  return render(request, 'recipes/detail.html', {
    'recipe': recipe
  })

class RecipeCreate(LoginRequiredMixin, CreateView):
  model = Recipe
  fields = ['name', 'ingredients', 'description', 'directions','region']

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