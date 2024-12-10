from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from .models import PhoneBook
from django.db.models import Q


def index(request):
    search = SearchUserForm(request.GET)
    if 'search' in request.GET:
        query = request.GET['search'].capitalize()
        view_data = PhoneBook.objects.filter(
            Q(first_name__icontains=query) | Q(last_name__icontains=query) | Q(phone__icontains=query))
    else:
        view_data = PhoneBook.objects.all()
    context = {
        'title': 'Телефонная книга',
        'view_data': view_data,
        'serach': search
    }
    return render(request, 'phone_book/index.html', context)


def add(request):
    form = PhoneBookForm()
    if request.method == 'POST':
        form = PhoneBookForm(data=request.POST, instance=None)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {
        'title': 'Добавить',
        'form': form
    }
    return render(request, 'phone_book/add.html', context)


def view_profile(request, user_id):
    profile = get_object_or_404(PhoneBook, id=user_id)
    context = {
        'title': f'Профиль | {profile.first_name}',
        'profile': profile,
    }
    return render(request, 'phone_book/profile.html', context)


def del_user(request, user_id):
    profile = get_object_or_404(PhoneBook, id=user_id)
    profile.delete()
    return redirect('index')


def edit_user(request, user_id):
    profile = get_object_or_404(PhoneBook, id=user_id)
    form = PhoneBookForm(data=request.POST or None, instance=profile)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {
        'title': f'Изменить | {profile.first_name}',
        'form': form,
    }
    return render(request, 'phone_book/add.html', context)
