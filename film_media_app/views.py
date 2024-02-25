from django.shortcuts import render
from django.http import HttpResponse

# home page view
def home(request):
    return HttpResponse("<h1>Hello World</h1>")