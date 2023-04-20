from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Product


def index(request):
    products = Product.objects.all()
    item_name = request.GET.get('item-name')
    if item_name:
        products = Product.objects.filter(name__icontains=item_name)
    return render(request, 'shop/index.html', {'products': products})