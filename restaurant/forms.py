from .models import RestaurantModels
from django import forms


class RestaurantForm(forms.ModelForm):
    class Meta:
        model = RestaurantModels
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        if not cleaned_data['phone'].isdigit():
            self.add_error('phone', 'Номер телефона должен состоять только из цифр')

class SearchForm(forms.Form):
    query = forms.CharField(label='Поиск', required=False)
