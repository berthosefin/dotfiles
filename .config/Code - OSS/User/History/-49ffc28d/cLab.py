from django.db import models


class Person(models.Model):
    registration_number = models.CharField(max_length=10)
    last_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    