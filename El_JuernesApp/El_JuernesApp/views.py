import codecs
import json
from urllib.request import urlopen

from django.shortcuts import render

from Layout_designer.models import Published_Article
from Layout_designer.views import mediumSizePharagraphs, largeSizePharagraphs, getImages


def home(request):

    published = Published_Article.objects.all()
    context = {'published': published}

    return render(request , 'Home_News.html' , context)


def front_new(request,slug):
    front_new = Published_Article.objects.get(slug=slug)
    context = {}
    wordcount = len(front_new.body)

    json_obj = urlopen("http://enigmatic-waters-71955.herokuapp.com/api/images")
    reader = codecs.getreader("utf-8")
    json_data = json.load(reader(json_obj))

    context['url'] = json_data['images'][0]['imageUrl']
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