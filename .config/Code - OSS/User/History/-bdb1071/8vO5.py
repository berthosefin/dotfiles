from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at',]
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    description = models.TextField()
    category = models.ForeignKey(Category, related_name='category', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products', blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at',]
    
    def __str__(self):
        return self.name