from django.urls import path
from .views import IndexView, add, update


app_name = 'todos'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('add/', add, name='add'),
    path('<int:todo_id>/update', update, name='update'),
]