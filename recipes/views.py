from django.shortcuts import render
from django.http import HttpResponse



def home(request):
    return HttpResponse('UMA LINDA STRING')


def contato(request):
    return HttpResponse('Página de contato')


