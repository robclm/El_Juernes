from django.db import models

NEW = "Nova notícia"
ASSIGNED = "Assignada"
TO_VALIDATE = "Per validar"
ACCEPTED = "Acceptat"
REJECTED = "Rebutjada"
COMMENTED = "Comentat"

class New(models.Model):
    STATES = (
        (NEW, "Nova notícia"),
        (ASSIGNED, "Assignada"),
        (TO_VALIDATE, "Per validar"),
        (ACCEPTED, "Acceptat"),
        (REJECTED, "Rebutjada"),
        (COMMENTED, "Comentat")
    )

    slug = models.CharField(max_length=140)
    title = models.CharField(max_length=140)
    description = models.CharField(max_length=140)
    body = models.TextField()
    type = models.CharField(max_length=140)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    assigned = models.CharField(max_length=140,default="Cap redactor assignat")
    limit_date = models.DateTimeField(null=True)
    countdown = models.CharField(max_length=140, null=True)
    priority = models.CharField(max_length=140, default="")
    state = models.CharField(max_length=140, default="Nova notícia", choices=STATES)

    def __str__(self):
        return 'New: ' + self.title


class Author(models.Model):
    username = models.CharField(max_length=140)
    bio = models.CharField(max_length=140)
    image = models.CharField(max_length=140)

    def __str__(self):
        return 'Author: ' + self.username
