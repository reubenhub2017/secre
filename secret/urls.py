from django.urls import path 
from . import views
from django.conf.urls import url
from django.conf import settings 
from django.contrib import static 


urlpatterns = [
   path('', views.index),
    path('r^login/$',views.login)
    url(r'^$', views.post name='post')

    

]
if setting.DEBUG: 
    urlpatterns += static(setting.STATIC_URL, document_root=settings.STATIC_ROOT)