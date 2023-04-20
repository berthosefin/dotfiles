from django.db import models


class Category(models.MOdel):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = 'categories'
    
    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, related_name=product, on_delete=models.CASCADE)
