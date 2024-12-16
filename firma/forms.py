from django import forms
from .models import *


class BuyerForm(forms.ModelForm):
    class Meta:
        model = BuyerModel
        fields = '__all__'


class SalesmanForm(forms.ModelForm):
    class Meta:
        model = SalesmanModel
        fields = '__all__'


class ProductForm(forms.ModelForm):
    class Meta:
        model = ProductModel
        fields = '__all__'


class SalesInfoForm(forms.ModelForm):
    class Meta:
        model = SalesInfoModel
        fields = ('buyer', 'salesman', 'product', 'date_sales', 'quantity')
