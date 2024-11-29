from django.urls import path, include
from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('1/', form_zadacha_1, name='form_zadacha_1'),
    path('2/', form_zadacha_2, name='form_zadacha_2'),
    path('3/', form_zadacha_3, name='form_zadacha_3'),
    path('4/', form_zadacha_4, name='form_zadacha_4'),
]
