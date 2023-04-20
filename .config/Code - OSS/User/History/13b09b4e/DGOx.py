from django.urls import path
from .views import add_n_show, remove


urlpatterns = [
    path('', add_n_show, name='student-add_n_show'),
    path('remove/<int:id>', remove, name='student-remove'),
]