from django.urls import path
from .views import IndexView, add


app_name = 'todos'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('add/', add, name='add'),
]