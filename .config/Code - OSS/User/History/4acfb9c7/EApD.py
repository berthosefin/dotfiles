from django.shortcuts import render
from .models import Product


def index(request):
    products = Product.objects.all()
    item_name = request.GET.get('item-name')
    if item_name != '' and item_name is not None:
        products = Product.objects.filter(title__icontains=item_name)
    return render(request, 'shop/index.html', {'products': products})