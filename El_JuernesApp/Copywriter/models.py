from django.db import models

from Graphic_reporter.models import Image


class Article(models.Model):
    slug = models.CharField(max_length=140)
    file = models.FileField(upload_to='articles')
    images = models.ManyToManyField(Image)

    def __str__(self):
        return 'Article: ' + self.slug
