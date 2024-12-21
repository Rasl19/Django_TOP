from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.db.models import Avg, Sum, Max, Min, Count


def index(request):
    return render(request, 'firma/index.html', {'title': 'Главная', })


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


# Отображение всех покупателей заданного продавца;

# def report(request):
#     form = SalesmanReportForm(request.POST or None)
#     context = {
#         'title': 'Вывод Информации',
#         'form': form,
#     }
#     if request.method == 'POST':
#         form = SalesmanReportForm(data=request.POST)
#         if form.is_valid():
#             salesman = get_object_or_404(SalesmanModel, id=int(form.cleaned_data['salesman']))
#             data = SalesInfoModel.objects.filter(salesman=salesman)
#             context['data'] = data
#     return render(request, 'firma/report.html', context)


def report(request):
    form = SalesmanReportForm(request.POST or None)
    context = {
        'title': 'Вывод Информации',
    }
    if request.method == 'POST':
        # Отображение всех продаж на заданную дату
        # data = SalesInfoModel.objects.filter(date_sales='2024-12-17')

        # Отображение всех продавцов, которые продали заданный товар;
        # data = SalesInfoModel.objects.filter(product__name='Груша')

        # Отображение всех покупателей, которые купили заданный товар
        # data = SalesInfoModel.objects.filter(product__name='Груша')

        # Отображение общей суммы продаж в заданный день.
        # data = SalesInfoModel.objects.filter(date_sales='2024-12-17').aggregate(sum_sales = Sum('sum_sales', default=0))

        # Отобразить название самого продаваемого товара
        # data = SalesInfoModel.objects.values('product__name').annotate(total_quantity=Sum('quantity')).order_by(
        #     '-total_quantity').first()

        # Отобразить лучшего продавца.Критерий определения:
        # максимальная сумма продаж
        # P.S допишу корректнее задание максимальная ОБЩАЯ сумма продаж.
        # Просто человек может 10 продаж по 1$ сделать у него сумма = 10$
        # А человек один раз на 2$ продал он уже лучшим будет. Это неверно
        # data = SalesInfoModel.objects.values('salesman__name').annotate(total_sum_sales=Sum('sum_sales')).order_by(
        #     '-total_sum_sales').first()

        # Отобразить лучшего покупателя.
        # Критерий определения: максимальная ОБЩАЯ сумма покупок
        # data = SalesInfoModel.objects.values('buyer__name').annotate(sum_sales=Sum('sum_sales')).order_by(
        #     '-sum_sales').first()

        # Отобразить название самого продаваемого товара за
        # указанный промежуток времени;
        # data = SalesInfoModel.objects.filter(date_sales__gte='2024-12-1', date_sales__lte='2024-12-15').values(
        #     'product__name').annotate(total_product=Sum('quantity')).order_by('-total_product').first()

        # Отобразить лучшего продавца.
        # Критерий определения: максимальная ОБЩАЯ сумма продаж за указанный
        # промежуток времени
        # data = SalesInfoModel.objects.filter(date_sales__gte='2024-12-1', date_sales__lte='2024-12-15').values(
        #     'salesman__name').annotate(total_sum=Sum('sum_sales')).order_by('-total_sum').first()

        # Отобразить лучшего покупателя.
        # Критерий определения: максимальная ОБЩАЯ сумма покупок за указанный
        # промежуток времени
        data = SalesInfoModel.objects.filter(date_sales__gte='2024-12-1', date_sales__lte='2024-12-15').values(
            'buyer__name').annotate(total_sum=Sum('sum_sales')).order_by('-total_sum').first()

        context['data'] = data
    return render(request, 'firma/report.html', context)
