from django.shortcuts import render
from .models import Product


def index(request):
    products = Product.objects.all()
    item_name = request.GET.get('item-name')
    return render(request, 'shop/index.html', {'products': products})