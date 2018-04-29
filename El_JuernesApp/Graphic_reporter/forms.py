from django import forms

from Graphic_reporter.models import Image

POLITICS = "Política"
SPORTS = "Esports"
NATURE = "Natura"
MUSIC = "Musica"
ART = "Art"
VEHICLE = "Vehicle"
GAMES = "Videojocs"
OTHER = "Altres"


class UploadImageForm(forms.Form):
    CATEGORIES = (
        ('', '- - -'),
        (POLITICS, "Política"),
        (SPORTS, "Esports"),
        (NATURE, "Natura"),
        (MUSIC, "Musica"),
        (ART, "Art"),
        (VEHICLE, "Vehicle"),
        (GAMES, "Videojocs"),
        (OTHER, "Altres"),
    )

    name = forms.CharField(max_length=140,
                           label='Introdueix el nom de la imatge',
                           required=True)

    image = forms.ImageField(label='Selecciona una imatge',
                             required=True)

    category = forms.ChoiceField(label='Categoria',
                                 choices=CATEGORIES,
                                 required=True)

    def clean_name(self):
        return self.cleaned_data['name']

    def clean_image(self):
        return self.cleaned_data['image']

    def clean_category(self):
        return self.cleaned_data['category']


class SearchImageForm(forms.Form):
    CATEGORIES = (
        ('', 'Totes'),
        (POLITICS, "Política"),
        (SPORTS, "Esports"),
        (NATURE, "Natura"),
        (MUSIC, "Musica"),
        (ART, "Art"),
        (VEHICLE, "Vehicle"),
        (GAMES, "Videojocs"),
        (OTHER, "Altres"),
    )

    name = forms.CharField(max_length=140,
                           label='Nom',
                           required=False)

    category = forms.ChoiceField(label='Categoria',
                                 choices=CATEGORIES,
                                 required=False)

    def clean_name(self):
        return self.cleaned_data['name']

    def clean_category(self):
        return self.cleaned_data['category']


class EditImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['name', 'image', 'category']

    CATEGORIES = (
        ('', '- - -'),
        (POLITICS, "Política"),
        (SPORTS, "Esports"),
        (NATURE, "Natura"),
        (MUSIC, "Musica"),
        (ART, "Art"),
        (VEHICLE, "Vehicle"),
        (GAMES, "Videojocs"),
        (OTHER, "Altres"),
    )

    name = forms.CharField(max_length=140,
                           label='Nom',
                           required=True)

    image = forms.ImageField(label='Imatge', required=False,
                             widget=forms.FileInput)

    category = forms.ChoiceField(label='Categoria',
                                 choices=CATEGORIES,
                                 required=True)

    def clean_name(self):
        return self.cleaned_data['name']

    def clean_image(self):
        return self.cleaned_data['image']

    def clean_category(self):
        return self.cleaned_data['category']
