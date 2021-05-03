from django.shortcuts import render
from .models import Cat


def cats_index(request):
  cats = Cat.objects.all()
  return render(request, 'cats/index.html', {'cats': cats})

# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')