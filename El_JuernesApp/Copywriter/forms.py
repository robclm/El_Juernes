from django import forms

class ArticleForm(forms.Form):
    file = forms.FileField(label="Selecciona una imatge")

    def clean_file(self):
        return self.cleaned_data['file']