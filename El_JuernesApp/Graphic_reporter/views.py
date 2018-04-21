from django.shortcuts import render

from Graphic_reporter.models import Image


def News_assigned(request):
    template = 'Graphic_reporter/assigned_news.html'
    context = None

    return render(request, template, context)


def Image_bank(request):
    template = 'Graphic_reporter/image_bank.html'
    images = Image.objects.all()

    return render(request, template, {'images': images})
