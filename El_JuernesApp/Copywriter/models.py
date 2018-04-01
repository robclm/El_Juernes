from django.db import models

# Create your models here.

class Article(models.Model):
    slug = models.CharField(max_length=140)
    title = models.CharField(max_length=140)
    description = models.CharField(max_length=140)
    body = models.TextField()
    assigned = models.CharField(max_length=140, default="Cap redactor assignat")
    priority = models.CharField(max_length=140, default='')