from django.db import models


class Person(models.Model):
    registration_number = models.CharField(max_length=10)
    last_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    birth_date = models.DateField()
    email = models.EmailField()
    phone_number = models.CharField(max_length=32)
    friends = models.ManyToManyField('self')
    faculty = models.ForeignKey('Faculty', on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name + " " + self.last_name 

class Message(models.Model):
    author = models.ForeignKey('Person', on_delete=models.CASCADE)
    content = models.TextField()
    publication_date = models.DateField()

class Faculty(models.Model):
    name = models.CharField(max_length=30)
    color = models.CharField(max_length=6)

    def __str__(self):
        return self.name

class Campus(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=60)

    def __str__(self):
        return self.name

class Job(models.Model):
    title = models.CharField(max_length=30)

class Cursus(models.Model):
    title = models.CharField(max_length=30)

class Employee(Person):
    office = models.CharField(max_length=30)
    campus = models.ForeignKey('Campus', on_delete=models.CASCADE)
    job = models.ForeignKey('Job', on_delete=models.CASCADE)

class Student(Person):
    cursus = models.ForeignKey('Cursus', on_delete=models.CASCADE)
    year = models.IntegerField()
