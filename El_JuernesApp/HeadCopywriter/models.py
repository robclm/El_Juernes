# Create your models here.
from django.db import models

from AfeNews.models import New
from Graphic_reporter.models import Image


class Article_comentat(models.Model):
    slug = models.CharField(max_length=140)
    file = models.FileField(upload_to='commented_articles')

    def __str__(self):
        return 'Article: ' + self.slug


class Images_sended(models.Model):
    noticia = models.ForeignKey(New, on_delete=models.CASCADE)
    images = models.ManyToManyField(Image)

    def __str__(self):
        return 'Image_Request: ' + self.noticia.title
