from django.db import models


class Collection(models.Model):
    name = models.CharField(max_length=60)
    slug = models.SlugField()

    @classmethod
    def get_default_collection(cls):
        pass


class Task(models.Model):
    description = models.CharField(max_length=300)
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)