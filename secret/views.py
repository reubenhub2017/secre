from django.shortcuts import render
from django.http import HttpResponse 

# Create your views here.
def index(request):
    return HttpResponse("<h1>index</h1>")
def login(request):
    return HttpResponse("<h1>login</h1>")
def home(request):
    return HttpResponse("<h1>Home</h1>")

