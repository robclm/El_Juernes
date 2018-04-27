from django import forms

from Graphic_reporter.models import Image


class ImageForm(forms.Form):
    name = forms.CharField(max_length=140,
                           label="Introdueix el nom de la imatge")

    image = forms.ImageField(label='Selecciona una imatge')

    def clean_name(self):
        name = self.cleaned_data['name']

        return name

    def clean_image(self):
        image = self.cleaned_data['image']

        return image


class SearchImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['name', 'category']
        labels = {
            'name': 'Nom',
            'category': 'Categoria'

        }
