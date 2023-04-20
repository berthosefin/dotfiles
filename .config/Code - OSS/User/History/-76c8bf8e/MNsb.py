from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from shop import settings
from store.views import index, product_detail
from accounts.views import signup, logout_user


urlpatterns = [
    path('', index, name='index'),
    path('product/<str:slug>/', product_detail, name='product'),
    path('signup/', signup, name='signup'),
    path('logout/', logout_user, name='logout'),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
