from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at',]


class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    description = models.TextField()
    category = models.ForeignKey(Category, related_name='category', on_delete=models.CASCADE)
    image = models.CharField(max_length=5000)