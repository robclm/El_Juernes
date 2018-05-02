# Create your models here.
from django.db import models


class Article_comentat(models.Model):
    slug = models.CharField(max_length=140)
    file = models.FileField(upload_to='')

    def __str__(self):
        return 'Article: ' + self.slug
