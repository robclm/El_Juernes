from django import forms


class ImageForm(forms.Form):
    description = forms.CharField(max_length=140,
                                  label="Introdueix la descripció de la imatge")

    image = forms.ImageField(label='Selecciona una imatge')

    def clean_description(self):
        description = self.cleaned_data['description']

        return description

    def clean_image(self):
        image = self.cleaned_data['image']

        return image
