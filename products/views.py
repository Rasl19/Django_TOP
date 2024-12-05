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
            data = [name for name in PRODUCTS.keys() if query.lower() in name.lower()]
            context['maxPage'] = ceil(len(data) / 3)
            if page != context['maxPage']:
                diapazon = data[(page - 1) * 3:page*3]
            else:
                diapazon = data[(page - 1) * 3::]
            context['data'] = {i: PRODUCTS[i] for i in diapazon}
    context['form'] = form
    return render(request, 'products/index.html', context)
