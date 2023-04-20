from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Product


def index(request):
    products = Product.objects.all()
    q = request.GET.get('item-name')
    if q:
        products = Product.objects.filter(name__icontains=q)
    paginator = Paginator(products, 4)
    page = request.GET.get('page')
    products = paginator.get_page(page)
    return render(request, 'shop/index.html', {'products': products})