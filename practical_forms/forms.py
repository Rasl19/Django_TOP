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
