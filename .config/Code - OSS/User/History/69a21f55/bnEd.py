from django.urls import path
from .views import index, detail


urlpatterns = [
    path('', index, name='shop-index'),
    path('<int:pk>', detail, name='shop-detail'),
]