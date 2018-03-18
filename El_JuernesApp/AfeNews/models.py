from django.db import models

# Create your models here.

class New(models.Model):
    slug = models.CharField(max_length=140)
    title = models.CharField(max_length=140)
    description = models.CharField(max_length=140)
    body = models.TextField()
    type = models.CharField(max_length=140)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)

class Author(models.Model):
    username = models.CharField(max_length=140)
    bio = models.CharField(max_length=140)
    image = models.CharField(max_length=140)