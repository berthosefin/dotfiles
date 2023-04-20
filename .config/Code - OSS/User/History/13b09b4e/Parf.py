from django.urls import path
from .views import add_n_show


urlpatterns = [
    path('', add_n_show, name='student-index')
]