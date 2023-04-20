from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at',]