from django.urls import path


urlpatterns = [
    path('', index, name='index'),
    path('login/', login, name='login'),
]