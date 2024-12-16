from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *


def index(request):
    return render(request, 'firma/index.html', {'title': 'Главная',})


def buyer_view(request):
    data = BuyerModel.objects.all()
    context = {
        'title': 'Покупатели',
        'data': data,
    }
    return render(request, 'firma/buyer.html', context)


def salesman_view(request):
    data = SalesmanModel.objects.all()
    context = {
        'title': 'Продавцы',
        'data': data,
    }
    return render(request, 'firma/salesman.html', context)


def product_view(request):
    data = ProductModel.objects.all()
    context = {
        'title': 'Товары',
        'data': data,
    }
    return render(request, 'firma/product.html', context)


def sales_info_view(request):
    data = SalesInfoModel.objects.all()
    context = {
        'title': 'Продажи',
        'data': data,
    }
    return render(request, 'firma/sales_info.html', context)


def buyer_profile(request, id):
    profile = get_object_or_404(BuyerModel, id=id)
    context = {
        'title': f'Профиль | {profile.name}',
        'profile': profile,
    }
    return render(request, 'firma/profile/profile_buyer.html', context)


def salesman_profile(request, id):
    profile = get_object_or_404(SalesmanModel, id=id)
    profile.job_position = profile.get_job_position_display()
    context = {
        'title': f'Профиль | {profile.name}',
        'profile': profile,
    }
    return render(request, 'firma/profile/profile_salesman.html', context)


def product_profile(request, id):
    profile = get_object_or_404(ProductModel, id=id)
    context = {
        'title': f'Профиль | {profile.name}',
        'profile': profile,
    }
    return render(request, 'firma/profile/profile_product.html', context)


def sales_info_profile(request, id):
    profile = get_object_or_404(SalesInfoModel, id=id)
    context = {
        'title': f'{profile.buyer} | {profile.salesman}',
        'profile': profile,
    }
    return render(request, 'firma/profile/profile_sales_info.html', context)


def buyer_add(request):
    form = BuyerForm()
    if request.method == 'POST':
        form = BuyerForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('buyer_view')
    context = {
        'title': 'Добавление | Покупатель',
        'form': form,
    }
    return render(request, 'firma/form.html', context)


def salesman_add(request):
    form = SalesmanForm()
    if request.method == 'POST':
        form = SalesmanForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('salesman_view')
    context = {
        'title': 'Добавление | Продавец',
        'form': form,
    }
    return render(request, 'firma/form.html', context)


def product_add(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_view')
    context = {
        'title': 'Добавление | Продукт',
        'form': form,
    }
    return render(request, 'firma/form.html', context)


def sales_info_add(request):
    form = SalesInfoForm()
    if request.method == 'POST':
        form = SalesInfoForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('sales_info_view')
    context = {
        'title': 'Добавление | Информация',
        'form': form,
    }
    return render(request, 'firma/form.html', context)


def buyer_edit(request, id):
    buyer = get_object_or_404(BuyerModel, id=id)
    form = BuyerForm(data=request.POST or None, instance=buyer)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('buyer_view')
    context = {
        'title': 'Редактирование',
        'form': form,
    }
    return render(request, 'firma/form.html', context)


def salesman_edit(request, id):
    salesman = get_object_or_404(BuyerModel, id=id)
    form = SalesmanForm(data=request.POST or None, instance=salesman)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('salesman_view')
    context = {
        'title': 'Редактирование',
        'form': form,
    }
    return render(request, 'firma/form.html', context)


def product_edit(request, id):
    product = get_object_or_404(BuyerModel, id=id)
    form = SalesmanForm(data=request.POST or None, instance=product)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('product_view')
    context = {
        'title': 'Редактирование',
        'form': form,
    }
    return render(request, 'firma/form.html', context)


def sales_info_edit(request, id):
    sales_info = get_object_or_404(BuyerModel, id=id)
    form = SalesmanForm(data=request.POST or None, instance=sales_info)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('sales_info_view')
    context = {
        'title': 'Редактирование',
        'form': form,
    }
    return render(request, 'firma/form.html', context)


def buyer_delited(request, id):
    profile = get_object_or_404(BuyerModel, id=id)
    profile.delete()
    return redirect('buyer_view')


def salesman_delited(request, id):
    profile = get_object_or_404(SalesmanModel, id=id)
    profile.delete()
    return redirect('salesman_view')


def product_delited(request, id):
    profile = get_object_or_404(ProductModel, id=id)
    profile.delete()
    return redirect('product_view')


def sales_info_delited(request, id):
    profile = get_object_or_404(SalesInfoModel, id=id)
    profile.delete()
    return redirect('sales_info_view')
