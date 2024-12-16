from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('buyer/', buyer_view, name='buyer_view'),
    path('salesman/', salesman_view, name='salesman_view'),
    path('product/', product_view, name='product_view'),
    path('sales_info/', sales_info_view, name='sales_info_view'),
    path('buyer/<int:id>/', buyer_profile, name='buyer_profile'),
    path('salesman/<int:id>/', salesman_profile, name='salesman_profile'),
    path('product/<int:id>/', product_profile, name='product_profile'),
    path('sales_info/<int:id>/', sales_info_profile, name='sales_info_profile'),
    path('buyer/add/', buyer_add, name='buyer_add'),
    path('salesman/add/', salesman_add, name='salesman_add'),
    path('product/add/', product_add, name='product_add'),
    path('sales_info/add/', sales_info_add, name='sales_info_add'),
    path('buyer/<int:id>/edit/', buyer_edit, name='buyer_edit'),
    path('salesman/<int:id>/edit/', salesman_edit, name='salesman_edit'),
    path('product/<int:id>/edit/', product_edit, name='product_edit'),
    path('sales_info/<int:id>/edit/', sales_info_edit, name='sales_info_edit'),
    path('buyer/<int:id>/del/', buyer_delited, name='buyer_delited'),
    path('salesman/<int:id>/del/', salesman_delited, name='salesman_delited'),
    path('product/<int:id>/del/', product_delited, name='product_delited'),
    path('sales_info/<int:id>/del/', sales_info_delited, name='sales_info_delited'),
]
