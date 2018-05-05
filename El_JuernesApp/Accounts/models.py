from django.contrib.auth.models import User
from django.db import models

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

    def __str__(self):
        return 'User_profile: ' + self.user.username

class Subscriber(models.Model):
    user = models.OneToOneField(User_profile, on_delete=models.CASCADE)

    def __str__(self):
        return 'Subscriber: ' + self.user.user.username

class Copywriter(models.Model):
    user = models.OneToOneField(User_profile, on_delete=models.CASCADE)
    speciality = models.CharField(max_length=140, )

    def __str__(self):
        return 'Copywriter: ' + self.user.user.username

class Head_copywriter(models.Model):
    user = models.OneToOneField(User_profile, on_delete=models.CASCADE)

    def __str__(self):
        return 'Head_copywriter: ' + self.user.user.username

class Graphic_reporter(models.Model):
    user = models.OneToOneField(User_profile, on_delete=models.CASCADE)

    def __str__(self):
        return 'Graphic_reporter: ' + self.user.user.username

class Layout_designer(models.Model):
    user = models.OneToOneField(User_profile, on_delete=models.CASCADE)

    def __str__(self):
        return 'Layout_designer: ' + self.user.user.username
