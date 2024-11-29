from django import forms


class UserForm(forms.Form):
    name = forms.CharField(label='Имя')
    surname = forms.CharField(label='Фамилия')


class ForNumber(forms.Form):
    start = forms.IntegerField(label='Начало')
    end = forms.IntegerField(label='Конец')

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data['start'] >= cleaned_data['end']:
            self.add_error('end', 'Значение поля "Старт" больше или равно значению поля "Конец"')
        return cleaned_data


class SubscriptionNews(forms.Form):
    name = forms.CharField(label='Имя')
    surname = forms.CharField(label='Фамилия')
    age = forms.IntegerField(label='Возраст', min_value=1)
    CHOICES = [
        ('Муж', 'Муж'),
        ('Жен', 'Жен'),
    ]
    sex = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect, label='Пол')
    email = forms.EmailField(label='Email')
