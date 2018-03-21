from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Subscriber(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Copywriter(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    speciality = models.CharField(max_length=140, )


class Head_copywriter(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Graphic_reporter(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Machine_designer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
