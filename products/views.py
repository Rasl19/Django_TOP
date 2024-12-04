from django.shortcuts import render
from .forms import *
from .const import *


def products(request):
    context = {'title': 'Главная', }
    form = Products()

    if 'query' in request.GET:
        form = Products(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            context['data'] = {name: details for name, details in PRODUCTS.items() if query.lower() in name.lower()}
    else:
        context['form'] = form
    return render(request, 'products/index.html', context)
