from django.shortcuts import render, redirect, get_object_or_404
from store.models import Product, Cart, Order
from django.urls import reverse


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
    order, created = Order.objects.get_or_create(user=user, product=product)
    if created:
        cart.orders.add(order)
        cart.save()
    else:
        order.quantity += 1
        order.save()
    return redirect(reverse('product', kwargs={'slug': slug}))


def cart(request):
    cart = get_object_or_404(Cart, user=request.user)
    return render(request, 'store/cart.html', {'orders': cart.orders.all()})


def delete_card(request):
    if cart := request.user.cart:
        cart.orders.all().delete()
        cart.delete()
    return redirect('index')