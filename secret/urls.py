from django.urls import path 
from . import views
from django.conf.urls import url


urlpatterns = [
   path('', views.index),
    path('r^login/$',views.login)
    url(r'^$', views.post name='post')

    

]