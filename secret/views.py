from django.shortcuts import render
from django.http import HttpResponse 
from django.template import loader 
from .models import Post


# Create your views here.
def index(request):
    
    template = loader.get_template('page/index.html')
    context = None
    return HttpResponse(template.render(context, request))

def login(request):
    return HttpResponse("<h1>login</h1>")

def home(request):
    all_posts = Post.objects.all()
    template = loader.get_template('page/home.html')
    context = {
        'all_posts' : all_posts,
    }
    return HttpResponse(template.render(context,request))

