from django.db import models

from AfeNews.models import New

TO_DO = "To do"
SEND = "Send"
VALIDATED = "Validated"
TO_CHANGE = "To change"


class Image_request(models.Model):

    STATES=(
            (TO_DO, "To do"),
            (SEND, "Send"),
            (VALIDATED, "Validated"),
            (TO_CHANGE, "To change")
    )

    noticia = models.ForeignKey(New,on_delete=models.CASCADE)
    state = models.CharField(max_length=30,choices=STATES)
    comment = models.CharField(max_length=280,default="Cap comentari")

    def __str__(self):
        return 'Image_Request: ' + self.noticia.title


POLITICS = "Política"
SPORTS = "Esports"
NATURE = "Natura"
MUSIC = "Musica"
ART = "Art"
VEHICLE = "Vehicle"
GAMES = "Videojocs"
OTHER = "Altres"


class Image(models.Model):
    CATEGORIES = (
        (POLITICS, "Política"),
        (SPORTS, "Esports"),
        (NATURE, "Natura"),
        (MUSIC, "Musica"),
        (ART, "Art"),
        (VEHICLE, "Vehicle"),
        (GAMES, "Videojocs"),
        (OTHER, "Altres"),
    )

    name = models.CharField(max_length=140)
    image = models.ImageField(upload_to='images')
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    category = models.CharField(max_length=30, choices=CATEGORIES, null=True)
    request_img = models.ManyToManyField(Image_request)

    def __str__(self):
        return 'Image: ' + self.name



