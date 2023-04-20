from django.contrib import admin
from django.urls import path

import tasks.views as views


urlpatterns = [
    path('', views.index, name="home"),
    path('add-collection', views.add_collection, name="add-collection"),
    path('admin/', admin.site.urls),
]
