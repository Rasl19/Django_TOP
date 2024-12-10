from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('add/', add, name='add'),
    path('<int:user_id>/', view_profile, name='view_profile'),
    path('del/<int:user_id>/', del_user, name='del'),
    path('edit/<int:user_id>/', edit_user, name='edit'),
]
