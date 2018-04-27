from django.shortcuts import render

from Graphic_reporter.forms import ImageForm
from Graphic_reporter.models import Image


def news_assigned(request):
    template = 'Graphic_reporter/assigned_news.html'
    context = None

    return render(request, template, context)


def image_bank(request):
    template = 'Graphic_reporter/image_bank.html'
    search_query = ""

    # Display all images
    images = Image.objects.all()

    # Upload Images
    if request.method == 'POST':
        form = ImageForm(request.POST or None, request.FILES or None)

        if form.is_valid():
            img_post = Image()

            img_post.description = form.clean_description()
            img_post.image = form.clean_image()

            img_post.save()
    else:
        # Search if there is something to search
        search_query = request.GET.get('search_box', '')

        if search_query is not None:
            images = images.filter(description__icontains=search_query)

    # Form to update images
    form = ImageForm()

    return render(request, template, {'images': images, 'form': form, 'search_query': search_query})
