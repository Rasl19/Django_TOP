from django.shortcuts import render
from .forms import *
from .const import *


def login(request):
    context = {'title': 'Вход', }
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


def calculate(request):
    context = {'title': 'Калькулятор', }
    if request.method == 'POST':
        form = CalculateForm(request.POST)
        if form.is_valid():
            num_1 = form.cleaned_data['num_1']
            num_2 = form.cleaned_data['num_2']
            num_3 = form.cleaned_data['num_3']
            operation = form.cleaned_data['operation']

            if operation == 'sum':
                result = num_1 + num_2 + num_3
            elif operation == 'product':
                result = num_1 * num_2 * num_3
            elif operation == 'average':
                result = round(((num_1 + num_2 + num_3) / 3), 2)
            context['data'] = result
            return render(request, 'practical_forms/calculate.html', context)
        else:
            context['form'] = form
            return render(request, 'practical_forms/calculate.html', context)
    form = CalculateForm()
    context['form'] = form
    return render(request, 'practical_forms/calculate.html', context)
