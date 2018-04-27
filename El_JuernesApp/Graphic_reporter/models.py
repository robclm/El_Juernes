from django.db import models

POLITICS = "Política"
SPORTS = "Esports"
NATURE = "Natura"
MUSIC = "Musica"
ART = "Art"
VEHICLE = "Vehicle"
OTHER = "Altres"


class Image(models.Model):
    CATEGORIES = (
        (POLITICS, "Política"),
        (SPORTS, "Esports"),
        (NATURE, "Natura"),
        (MUSIC, "Musica"),
        (ART, "Art"),
        (VEHICLE, "Vehicle"),
        (OTHER, "Altres"),
    )

    name = models.CharField(max_length=140)
    image = models.ImageField(upload_to='')
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    category = models.CharField(max_length=30, choices=CATEGORIES, null=True)


    def __str__(self):
        return 'Image: ' + self.name
