from django.contrib.auth.models import User
from django.db import models


# Create your models here.
SUBSCRIBER = "Subscriber"
COPYWRITER = "Copywriter"
HEAD_COPYWRITER = "Head_copywriter"
GRAPHIC_REPORTER = "Graphic_reporter"
MACHINE_DESIGNER = "Layout_designer"


class User_profile(models.Model):
    ROLES = (
        (SUBSCRIBER, "Subscriber"),
        (COPYWRITER, "Copywriter"),
        (HEAD_COPYWRITER, "Head_copywriter"),
        (GRAPHIC_REPORTER, "Graphic_reporter"),
        (MACHINE_DESIGNER, "Layout_designer"),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=30, choices=ROLES)


class Subscriber(models.Model):
    user = models.OneToOneField(User_profile, on_delete=models.CASCADE)


class Copywriter(models.Model):
    user = models.OneToOneField(User_profile, on_delete=models.CASCADE)
    speciality = models.CharField(max_length=140, )


class Head_copywriter(models.Model):
    user = models.OneToOneField(User_profile, on_delete=models.CASCADE)


class Graphic_reporter(models.Model):
    user = models.OneToOneField(User_profile, on_delete=models.CASCADE)


class Layout_designer(models.Model):
    user = models.OneToOneField(User_profile, on_delete=models.CASCADE)
