from django.urls import path, include
from .views import *



urlpatterns = [
    path('login/', login, name='login'),
    path('calculate/', calculate, name='calculate'),
    path('registre/', registre, name='registre'),
    path('day_programm/', day_programming, name='day_programming'),
]