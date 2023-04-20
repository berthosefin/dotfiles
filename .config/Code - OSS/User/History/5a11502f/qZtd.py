from django.shortcuts import render, get_object_or_404
from store.models import Product, Cart


def index(request):
    products = Product.objects.all()
    return render(request, 'store/index.html', {'products': products})


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'store/detail.html', {'product': product})


def add_to_cart(request, slug):
    user = request.user
    product = get_object_or_404(Product, slug=slug)
    cart, _ = Cart.objects.get_or_create(user=user)