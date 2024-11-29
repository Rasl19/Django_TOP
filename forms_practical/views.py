from django.shortcuts import render, redirect
from .forms import *


def index(request):
    return render(request, 'forms_practical/index.html')

def form_zadacha_1(request):
    context = {
        'title': 'Good Day',
    }
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            context['data'] = data
            return render(request, 'forms_practical/form_zadacha_1.html', context)
        else:
            context['form'] = form
            return render(request, 'forms_practical/form_zadacha_1.html', context)
    form = UserForm()
    context['form'] = form
    return render(request, 'forms_practical/form_zadacha_1.html', context)

def form_zadacha_2(request):
    context = {
        'title': 'ForNumber',
    }
    # Если POST запрос
    if request.method == 'POST':
        form = ForNumber(request.POST)
        # Проверка на валидность
        if form.is_valid():
            simple_number = []
            data = form.cleaned_data
            for i in range(data['start'], data['end'] + 1):
                flag = True
                if i == 1:
                    simple_number.append(i)
                    continue
                for j in range(2, i):
                    if i % j == 0:
                        flag = False
                        break
                if flag:
                    simple_number.append(i)
            context['data'] = simple_number
            return render(request, 'forms_practical/form_zadacha_2.html', context)
        else:
            context['form'] = form
            return render(request, 'forms_practical/form_zadacha_2.html', context)
    form = ForNumber()
    context['form'] = form
    return render(request, 'forms_practical/form_zadacha_2.html', context)

def form_zadacha_3(request):
    context = {'title': 'Подписка',}
    if request.method == 'POST':
        form = SubscriptionNews(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            context['data'] = data
            return render(request, 'forms_practical/form_zadacha_3.html', context)
        else:
            context['form'] = form
            return render(request, 'forms_practical/form_zadacha_3.html', context)
    form = SubscriptionNews()
    context['form'] = form
    return render(request, 'forms_practical/form_zadacha_3.html', context)
