from django.shortcuts import render
from django.http import HttpResponse



def home(request):
    context = {'name': 'eoq mlk'}
    return render(request, 'recipes/pages/home.html', context)

