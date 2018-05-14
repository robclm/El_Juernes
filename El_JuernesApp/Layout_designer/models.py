# Create your models here.
from django.db import models
from Graphic_reporter.models import Image


class Published_Article(models.Model):
    slug = models.CharField(max_length=140)
    title = models.CharField(max_length=140)
    description = models.CharField(max_length=140)
    body = models.TextField()
    images = models.ManyToManyField('Graphic_reporter.Image')


    def __str__(self):
        return 'Publised Article: ' + self.slug