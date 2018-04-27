from django.db import models

class New(models.Model):
    slug = models.CharField(max_length=140)
    title = models.CharField(max_length=140)
    description = models.CharField(max_length=140)
    body = models.TextField()
    type = models.CharField(max_length=140)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    assigned = models.CharField(max_length=140,default="Cap redactor assignat")
    priority = models.CharField(max_length=140, default="")
    tovalidate = models.BooleanField(default=False)

    def __str__(self):
        return 'New: ' + self.title


class Author(models.Model):
    username = models.CharField(max_length=140)
    bio = models.CharField(max_length=140)
    image = models.CharField(max_length=140)

    def __str__(self):
        return 'Author: ' + self.username
