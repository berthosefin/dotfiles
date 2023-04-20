from django.urls import path, include

from product import views


urlpatterns = [
    path('latest-project/', views.LatestProductsList.as_view()),
]