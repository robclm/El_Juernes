from django.db import models



class Image(models.Model):
    description = models.CharField(max_length=140)
    image = models.ImageField(upload_to='')

    def __str__(self):
        return 'Image: ' + self.description


