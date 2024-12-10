from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.db.models import Q


def index(request):
    search = SearchForm(request.GET)
    data = RestaurantModels.objects.all()
    if 'query' in request.GET:
        query = request.GET['query'].capitalize()
        data = RestaurantModels.objects.filter(Q(name__icontains=query) | Q(specialization__icontains=query))
    context = {
        'title': 'Главная',
        'search': search,
        'data': data,
    }
    return render(request, 'restaurant/index.html', context)


def add(request):
    form = RestaurantForm()
    if request.method == 'POST':
        form = RestaurantForm(data=request.POST, instance=None)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {
        'title': 'Добавление',
        'form': form,
    }
    return render(request, 'restaurant/add.html', context)


def restaurant_profile(request, id):
    profile = get_object_or_404(RestaurantModels, id=id)
    context = {
        'title': 'Профиль',
        'data': profile
    }
    return render(request, 'restaurant/profile.html', context)


def edit(request, id):
    profile = get_object_or_404(RestaurantModels, id=id)
    form = RestaurantForm(data=request.POST or None, instance=profile)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('profile', profile.id)
    context = {
        'title': 'Изменить',
        'form': form,
    }
    return render(request, 'restaurant/add.html', context)


def delite(request, id):
    profile = get_object_or_404(RestaurantModels, id=id)
    profile.delete()
    return redirect('index')
