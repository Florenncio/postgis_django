from django.db import models

class Blog (models.Model):
    name = models.CharField(max_length=100)

class Author(models.Model):
    name = models.CharField(max_length=200)

class Entry(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE),
    authors =  models.ManyToManyField(Author),
    headline = models.CharField(max_length=255)