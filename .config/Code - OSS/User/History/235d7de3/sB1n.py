from rest_framework import serializers
from .models import Category, Product

class ProductSerializer(serializers.ModelSerialize):
    class Meta:
        model = Product
        fields = {
            "id",
            "name",
            "get_absolute_url",
            "description",
            "price",
            "get_image",
            "get_thumbnail"
        }