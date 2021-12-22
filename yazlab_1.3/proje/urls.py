from django.conf.urls import url
from .views import *

app_name = "proje"

urlpatterns = [

    url(r'^index/$', proje_index, name="index"),
    
    url(r'^create/$', proje_create, name='create'),


]
