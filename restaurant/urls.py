from django.urls import path, include
from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('add/', add, name='add'),
    path('<int:id>/', restaurant_profile, name='profile'),
    path('edit/<int:id>/', edit, name='edit'),
    path('del/<int:id>/', delite, name='delite'),
]
