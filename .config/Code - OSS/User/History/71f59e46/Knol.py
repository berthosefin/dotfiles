from django.db import models


class Collection(models.Model):
    name = models.CharField(max_length=60)
    slug = models.SlugField()


class Task(models.Model):
    description = models.CharField(max_length=300)
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)