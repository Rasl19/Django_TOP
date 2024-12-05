from django.shortcuts import render
from .forms import *
from .const import *
from math import ceil


def products(request):
    context = {'title': 'Главная', }
    form = Products()
    page = int(request.GET.get('page', 1))
    context['page'] = page
    context['nextPage'] = page + 1
    context['prevPage'] = page - 1

    if 'query' in request.GET:
        form = Products(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            context['query'] = query
            # context['data'] = {name: details for name, details in PRODUCTS.items() if query.lower() in name.lower()}
            context['data'] = {name: details for name, details in PRODUCTS.items() if query.lower() in name.lower()}
            context['maxPage'] = ceil(len(context['data']) / 3)

    context['form'] = form
    return render(request, 'products/index.html', context)



# def products(request):
#     context = {'title': 'Главная', }
#     form = Products()
#
#     if 'query' in request.GET:
#         form = Products(request.GET)
#         if form.is_valid():
#             query = form.cleaned_data['query']
#             context['data'] = {name: details for name, details in PRODUCTS.items() if query.lower() in name.lower()}
#     else:
#         context['form'] = form
#     return render(request, 'products/index.html', context)
