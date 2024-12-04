from django.urls import path, include
from .views import *

urlpatterns = [
    path('index/', products, name='index'),
]