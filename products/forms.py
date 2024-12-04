from django import forms



class Products(forms.Form):
    query = forms.CharField(label='Поиск')
