from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Product


def index(request):
    products = Product.objects.all()
    item_name = request.GET.get('item-name')
    if item_name:
        products = Product.objects.filter(name__icontains=item_name)
    paginator = Paginator(products, 4)
    page = request.GET.get('page')
    products = paginator.get_page(page)
    return render(request, 'shop/index.html', {'products': products})