from django.forms import ModelForm
from .models import PhoneBook
from django import forms


class PhoneBookForm(ModelForm):
    def clean(self):
        cleaned_data = super().clean()
        if len(cleaned_data['phone']) != 11:
            self.add_error('phone', 'Номер телефона должен состоять из 11 цифр')

        elif not cleaned_data['phone'].isdigit():
            self.add_error('phone', 'Номер телефона должен состоять из цифр')

        elif cleaned_data['phone'][0] != '7':
            self.add_error('phone', 'Номер телефона должен начинаться с 7')

    class Meta:
        model = PhoneBook
        fields = '__all__'


class SearchUserForm(forms.Form):
    search = forms.CharField(label='Поиск', required=False)
