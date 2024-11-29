from django import forms
from .const import *


class UserLogin(forms.Form):
    login = forms.CharField(label='Логин')
    password = forms.CharField(label='Пароль')

    def clean(self):
        cleaned_data = super().clean()
        # Проверка на наличе пользователя
        if cleaned_data['login'] in USERS:
            # Проверка данных
            if cleaned_data['password'] == USERS[cleaned_data['login']]['password']:
                return cleaned_data
            else:
                self.add_error('password', 'Неверный пароль')
        else:
            self.add_error('login', 'Пользователя с таким логином не существует')


class CalculateForm(forms.Form):
    num_1 = forms.IntegerField(label='Число 1')
    num_2 = forms.IntegerField(label='Число 2')
    num_3 = forms.IntegerField(label='Число 3')

    CHOICES = [
        ('sum', 'Сумма'),
        ('product', 'Произведение'),
        ('average', 'Среднее'),
    ]
    operation = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect, label='Операция')


class UserRegistre(forms.Form):
    name = forms.CharField(label='Имя', required=True)
    surname = forms.CharField(label='Фамилия', required=True)
    age = forms.IntegerField(label='Возраст', min_value=1, max_value=120)
    email = forms.EmailField(label='Email')
    CHOICES = [
        ('Муж', 'Муж'),
        ('Жен', 'Жен'),
    ]
    sex = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect, label='Пол')
    delivery_address = forms.CharField(label='Адрес доставки')
    subscribe_newsletter = forms.BooleanField(label='Получать новости компании', required=False)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        return email


class YearProgramming(forms.Form):
    year = forms.IntegerField(label='Год', min_value=1900, max_value=2100)
