from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('writers/', writers, name='writers'),
    path('best_books/', best_books, name='best_books'),
    path('writers/<str:writer_name>/', writers_name, name='writers_name'),
    path('best_books/<int:number_book>/', best_book_info, name='top_book'),
    path('writers/<str:writer_name>/<str:name_book>/', book_info, name='book_info'),
]
