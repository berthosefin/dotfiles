from django.urls import path
from .views import add_n_show, remove, modify


urlpatterns = [
    path('', add_n_show, name='student-add_n_show'),
    path('modify/<int:id>', modify, name='student-modify'),
    path('remove/<int:id>', remove, name='student-remove'),
]