from django.urls import path, include
from website.views import *

app_name = 'website'

urlpatterns = [
    path('', index_view, name= 'home')
]