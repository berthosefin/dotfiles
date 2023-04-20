from django.shortcuts import render
from .models import Category, Product


def all_products(request):
    product = Product.objects.all()