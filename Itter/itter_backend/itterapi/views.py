from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def default_index(request):
    return HttpResponse("<h1>Hey site is working, maybe</h1>")