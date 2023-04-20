from django.shortcuts import render, get_object_or_404
from store.models import Product


def index(request):
    products = Product.objects.all()
    return render(request, 'store/index.html', {'products': products})

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)