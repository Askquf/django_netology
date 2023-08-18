from django.db.models.functions import Coalesce
from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')

def show_catalog(request):
    template = 'catalog.html'
    sort_value = request.GET.get('sort', 'name')
    if sort_value == 'max_price':
        phones = Phone.objects.order_by('-price')
    elif sort_value == 'min_price':
        phones = Phone.objects.order_by('price')
    else:
        phones = Phone.objects.order_by('name')
    context = {
        'phones': phones
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    context = {
        'phone': Phone.objects.get(slug=slug)
    }
    return render(request, template, context)
