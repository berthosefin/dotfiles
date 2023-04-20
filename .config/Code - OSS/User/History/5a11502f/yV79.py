from django.shortcuts import render
from store.models import Product


def index(request):
    return render(request, 'store/index.html')