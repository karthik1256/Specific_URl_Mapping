from black.views import *
from django.urls import path

app_name='anything'
urlpatterns=[
    
    path('chandra/',chandra,name='chandra'),
]