from django.shortcuts import render
from django.http import HttpResponse



def home(request):
    context = {'name': 'joao'}
    return render(request, 'recipes/pages/home.html', context)


def recipes(request, id):
    context = {'name': 'joao'}
    return render(request, 'recipes/pages/recipe-view.html', context)

