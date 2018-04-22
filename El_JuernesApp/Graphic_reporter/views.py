from django.shortcuts import render

from Graphic_reporter.forms import ImageForm
from Graphic_reporter.models import Image


def News_assigned(request):
    template = 'Graphic_reporter/assigned_news.html'
    context = None

    return render(request, template, context)


def Image_bank(request):
    template = 'Graphic_reporter/image_bank.html'
    images = Image.objects.all()

    if request.method == 'POST':
        form = ImageForm(request.POST or None, request.FILES or None)

        if form.is_valid():
            img_post = Image()

            img_post.description = form.clean_description()
            img_post.image = form.clean_image()

            img_post.save()

    form = ImageForm()

    return render(request, template, {'images': images, 'form': form})
