from django.urls import path, include
from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('1/', form_zadacha_1, name='form_zadacha_1'),
    path('2/', form_zadacha_2, name='form_zadacha_2'),
]
