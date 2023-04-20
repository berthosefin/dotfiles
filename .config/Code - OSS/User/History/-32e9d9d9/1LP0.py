from django.db import models


'''
Product:
- Nom
- Prix
- La quantité en stock
- Description
- Image
'''
class Product(models.Model):
    name = models.CharField(max_length=128)