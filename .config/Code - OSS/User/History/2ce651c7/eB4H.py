from django.urls import path
from .views import IndexView, add, update, delete


app_name = 'todos'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('add/', add, name='add'),
    path('<int:todo_id>/update', update, name='update'),
    path('<int:todo_id>/delete', delete, name='delete'),
]