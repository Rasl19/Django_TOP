from django.shortcuts import render
from .forms import *
from .const import *


def login(request):
    context = {'title': 'Вход',}
    if request.method == 'POST':
        form = UserLogin(request.POST)
        if form.is_valid():
            # В данные также добавляем уровень пользователя
            form.cleaned_data['level'] = USERS[form.cleaned_data['login']]['level']
            data = form.cleaned_data
            context['data'] = data
            return render(request, 'practical_forms/login.html', context)
        else:
            context['form'] = form
            return render(request, 'practical_forms/login.html', context)
    form = UserLogin()
    context['form'] = form
    return render(request, 'practical_forms/login.html', context)
