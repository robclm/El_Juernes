from django.contrib.auth.models import User
from django.shortcuts import render
from django.utils import timezone
from django.views import generic
from Layout_designer.models import Published_Article
from Layout_designer.views import mediumSizePharagraphs,largeSizePharagraphs,getImages



def home(request):

    published = Published_Article.objects.all()
    context = {'published': published}

    return render(request,'Home_News.html',context)


def front_new(request,slug):
    front_new = Published_Article.objects.get(slug=slug)
    context = {}
    wordcount = len(front_new.body)

    context['title']=front_new.title
    context['description']=front_new.description

    if wordcount <= 100:

        context['firstparagraph'] = front_new.body
        context['firstparagraph1'],context['firstparagraph2'] = mediumSizePharagraphs(front_new.body)

    elif 100 < wordcount <= 400:

        context['firstparagraph'],\
        context['secondparagraph'] = mediumSizePharagraphs(front_new.body)

        context['firstparagraph1'],context['firstparagraph2'] = mediumSizePharagraphs(context['firstparagraph'])

        try:
            context['image1'] = getImages(1,slug)
        except:
            """Nothing"""

    elif wordcount > 400:

        context['firstparagraph'], context['secondparagraph'], \
        context['thirdparagraph'] = largeSizePharagraphs(front_new.body)

        context['firstparagraph1'], context['firstparagraph2'] = mediumSizePharagraphs(context['firstparagraph'])


        try:
            context['image1'], context['image2'] = getImages(2, slug)
        except:

            try:
                context['image1'] = getImages(1, slug)
            except:
                """Nothing"""

    return render(request,'front_new.html',context)