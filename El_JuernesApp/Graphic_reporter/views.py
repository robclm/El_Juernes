from django.shortcuts import render, redirect

from Graphic_reporter.forms import ImageForm, SearchImageForm
from Graphic_reporter.models import Image


def news_assigned(request):
    template = 'Graphic_reporter/assigned_news.html'
    context = None

    return render(request, template, context)


def image_bank(request):
    template = 'Graphic_reporter/image_bank.html'
    search_category_form = SearchImageForm

    # Display all images
    images = Image.objects.all()

    # Search if there is something to search
    search_name_query = request.GET.get('search_name_box', '')
    search_category_query = request.GET.get('search_category_box', '')

    if search_name_query is not None:
        images = images.filter(name__icontains=search_name_query,
                               category__icontains=search_category_query)

    # Form to update images
    image_form = ImageForm()

    return render(request, template, {'images': images,
                                      'image_form': image_form,
                                      'search_category_form': search_category_form,
                                      'search_name_query': search_name_query,
                                      'search_category_query': search_category_query})


def upload_images(request):
    template = 'Graphic_reporter/upload_images.html'

    # Upload Images
    if request.method == 'POST':
        image_form = ImageForm(request.POST or None, request.FILES or None)

        if image_form.is_valid():
            img_post = Image()

            img_post.name = image_form.clean_name()
            img_post.image = image_form.clean_image()

            img_post.save()

            return redirect('gr_correct_upload')
    else:
        # Show empty form
        image_form = ImageForm()

    return render(request, template, {'image_form': image_form})
