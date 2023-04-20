from django.contrib import admin
from .models import Category, Product


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('nama', 'created_at',)


admin.site.register(Category)
admin.site.register(Product)