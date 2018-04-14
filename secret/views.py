from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.shortcuts import redirect
from django.template import loader 
from .models import Post
#from .forms import loginform


from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    #loginout,
    ) 
# Create your views here.
def index(request):
    
    template = loader.get_template('page/index.html')
    context = None
    return HttpResponse(template.render(context, request))

def login_view(request):
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        password = form.cleaned_data.get('password')
    return render(request, "home.html")

def home(request):
    all_posts = Post.objects.all()
    template = loader.get_template('page/home.html')
    context = {
        'all_posts' : all_posts,
    }
    return HttpResponse(template.render(context,request))

def get_login(request):
    if request.method=="POST":
        form = loginform(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('home.html')
        else:
            form = loginform()
            return render(request,index.html,{'form': form})
        