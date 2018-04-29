from django.shortcuts import render, redirect

from Graphic_reporter.forms import UploadImageForm, SearchImageForm, EditImageForm
from Graphic_reporter.models import Image


def news_assigned(request):
    template = 'Graphic_reporter/assigned_news.html'
    context = None

    return render(request, template, context)


def image_bank(request):
    template = 'Graphic_reporter/image_bank.html'

    # Display all images
    images = Image.objects.all()

    # Search images
    if request.method == "POST":
        search_images_form = SearchImageForm(request.POST)

        if search_images_form.is_valid():
            name = search_images_form.clean_name()
            category = search_images_form.clean_category()

            images = images.filter(name__icontains=name,
                                   category__icontains=category)
    else:
        # Empty search form
        search_images_form = SearchImageForm()

    return render(request, template, {'images': images,
                                      'search_images_form': search_images_form})


def upload_image(request):
    template = 'Graphic_reporter/upload_image.html'

    # Upload Image
    if request.method == 'POST':
        image_form = UploadImageForm(request.POST or None, request.FILES or None)

        if image_form.is_valid():
            img_post = Image()

            img_post.name = image_form.clean_name()
            img_post.image = image_form.clean_image()
            img_post.category = image_form.clean_category()

            img_post.save()

            return redirect('gr_correct_upload')
    else:
        # Show empty form
        image_form = UploadImageForm()

    return render(request, template, {'upload_image_form': image_form})


def edit_image(request, pk):
    template = 'Graphic_reporter/edit_image.html'
    image = Image.objects.get(pk=pk)

    # Edit Image
    if request.method == 'POST':
        edit_image_form = EditImageForm(request.POST, request.FILES, instance=image)

        if edit_image_form.is_valid():

            image.name = edit_image_form.clean_name()
            image.category = edit_image_form.clean_category()

            if edit_image_form.clean_image() is not None:
                image.image = edit_image_form.clean_image()

            image.save()

            return redirect('gr_correct_edit')

    else:
        # Image to edit
        edit_image_form = EditImageForm(instance=image)

    return render(request, template, {'edit_image_form': edit_image_form,
                                      'image': image})
