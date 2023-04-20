from django.db import models


class Collection(models.Model):
    name = models.CharField(max_length=60)
    slug = models.SlugField()

    @classmethod
    def get_default_collection(cls) -> "Collection":
        collection, _ = cls.objects.get_or_create(name="Default", slug="_default")
        return collection


class Task(models.Model):
    description = models.CharField(max_length=300)
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)