from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from shop import settings
from store.views import index, product_detail


urlpatterns = [
    path('', index, name='index'),
    path('product/<str:slug>/', product_detail, name='product'),
    path('signup/', signup),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
