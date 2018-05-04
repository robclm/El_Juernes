from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from Graphic_reporter.forms import UploadImageForm, SearchImageForm, EditImageForm
from Graphic_reporter.models import *


@login_required(login_url='/accounts/login')
def news_assigned(request):
    # Check if the role is correct
    if not role_is_graphic_reporter(request.user.username):
        return redirect('access_denied')

    template = 'Graphic_reporter/assigned_news.html'

    all_requests = Image_request.objects.all()
    requests_to_do = all_requests.filter(state__exact='To do',
                                         )

    context = {'requests': requests_to_do}

    return render(request, template, context)


@login_required(login_url='/accounts/login')
def images_new_request(request, pk):
    if not role_is_graphic_reporter(request.user.username):
        return redirect('access_denied')

    template = 'Graphic_reporter/images_new_request.html'

    image_request = Image_request.objects.get(pk=pk)

    context = {'image_request': image_request}

    return render(request, template, context)


@login_required(login_url='/accounts/login')
def image_bank(request):
    # Check if the role is correct
    if not role_is_graphic_reporter(request.user.username):
        return redirect('access_denied')

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


@login_required(login_url='/accounts/login')
def upload_image(request):
    # Check if the role is correct
    if not role_is_graphic_reporter(request.user.username):
        return redirect('access_denied')

    template = 'Graphic_reporter/upload_image.html'

    # Check the role is correct
    if not role_is_graphic_reporter(request.user.username):
        return redirect('access_denied')

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


@login_required(login_url='/accounts/login')
def edit_image(request, pk):
    # Check if the role is correct
    if not role_is_graphic_reporter(request.user.username):
        return redirect('access_denied')

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


@login_required(login_url='/accounts/login')
def select_images(request, pk):
    # Check if the role is correct
    if not role_is_graphic_reporter(request.user.username):
        return redirect('access_denied')

    template = 'Graphic_reporter/select_images.html'

    image_request = Image_request.objects.get(pk=pk)
    all_images = Image.objects.all()

    if request.method == "POST":

        # Select images to send
        select_image_pk = 'selected_image' in request.POST and request.POST['selected_image']

        if select_image_pk != False:
            selected_image = all_images.get(pk=select_image_pk)
            image_request.images.add(selected_image)
            image_request.save()

        # Eliminate images to send
        eliminate_image_pk = 'eliminated_image' in request.POST and request.POST['eliminated_image']

        if eliminate_image_pk != False:
            eliminate_image_pk = all_images.get(pk=eliminate_image_pk)
            image_request.images.remove(eliminate_image_pk)
            image_request.save()

        # Search images
        search_images_form = SearchImageForm(request.POST)

        if search_images_form.is_valid():
            name = search_images_form.clean_name()
            category = search_images_form.clean_category()

            all_images = all_images.filter(name__icontains=name,
                                           category__icontains=category)

    else:
        # Empty search form
        search_images_form = SearchImageForm()

    images_to_send = image_request.images.all()

    return render(request, template, {'images': all_images,
                                      'search_images_form': search_images_form,
                                      'image_request': image_request,
                                      'images_to_send': images_to_send})


@login_required(login_url='/accounts/login')
def send_images(request, pk):
    # Check if the role is correct
    if not role_is_graphic_reporter(request.user.username):
        return redirect('access_denied')

    template = 'Graphic_reporter/correct_send.html'

    image_request = Image_request.objects.get(pk=pk)
    image_request.state = 'Send'
    image_request.save()

    return render(request, template, {})


def role_is_graphic_reporter(username):
    # Check if the user is a graphic reporter
    user = User.objects.get(username=username)

    if user.user_profile.role == "Graphic_reporter":
        return True
    else:
        return False
