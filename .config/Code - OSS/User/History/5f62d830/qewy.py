from django.shortcuts import render
from django.http import HttpResponse
from tasks.models import Collection


def index(request):
    collections = Collection.objects.order_by('name')
    return render(request, 'tasks/index.html', context={})


def add_collection(request):
    collection_name = request.POST.get('collection-name')
    Collection.objects.create(name=collection_name)
    return HttpResponse()