from django.http import HttpResponse
from django.shortcuts import render
from AfeNews.models import New
from Copywriter.models import Article
from Graphic_reporter.models import Image
from Layout_designer.models import *

def getImages(number,slug):

    article = Article.objects.get(slug=slug)
    images = list(article.images.all())

    if number == 1:
        return images[0]

    elif number == 2:
        return images[0], images[1]


def mediumSizePharagraphs(articleBody):

    counter = 0
    totalphrases = articleBody.split(".")
    firstparagraph = ""
    secondparagraph = ""

    for phrase in totalphrases:
        if counter < (len(totalphrases) / 2):

            firstparagraph = firstparagraph + phrase + "."
            counter = counter + 1
        else:

            secondparagraph = secondparagraph + phrase + "."

    return firstparagraph,secondparagraph

def largeSizePharagraphs(articleBody):

    counter = 0
    totalphrases = articleBody.split(".")
    firstparagraph = ""
    secondparagraph = ""
    thirdparagraph = ""

    for phrase in totalphrases:
        if counter < (len(totalphrases) / 3):

            firstparagraph = firstparagraph + phrase + "."
            counter = counter + 1

        elif counter < ((len(totalphrases) / 3) * 2):
            secondparagraph = secondparagraph + phrase + "."
            counter = counter + 1

        else:
            thirdparagraph = thirdparagraph + phrase + "."

    return firstparagraph,secondparagraph,thirdparagraph



def getNewContext(slug,flag):

    context = {}

    if flag == 'new':
        context['new'] = New.objects.get(slug=slug)

    elif flag == 'article':
        context['article'] = Article.objects.get(slug=slug)

    elif flag == 'both':
        context['new'] = New.objects.get(slug=slug)
        context['article'] = Article.objects.get(slug=slug)

    return context

def news_assigned(request):
    template = 'Layout_designer/assigned_news.html'
    context = {'Acceptades': New.objects.filter(state="Acceptat")}

    return render(request, template, context)

def new_details(request,slug):
    context = getNewContext(slug,'both')

    template = 'Layout_designer/layout_new.html'
    return render(request, template, context)



def maquetar(request,slug):
    context = getNewContext(slug,'both')

    template = 'Layout_designer/layout_action.html'
    return render(request,template,context)

def preview(request,slug):

    editedArticleData = request.POST.dict()

    context = {}
    context['slug'] = editedArticleData['slug']
    context['title'] = editedArticleData['title']
    context['description'] = editedArticleData['description']

    template = ""
    toParse = editedArticleData['body']
    wordcount = toParse.split(" ")

    if len(wordcount) <= 100:

        template = 'Layout_designer/short.html'
        context['wordcount'] = len(wordcount)
        context['body'] = editedArticleData['body']

    elif 100 < len(wordcount) <= 400:

        template = 'Layout_designer/medium.html'
        context['wordcount'] = len(wordcount)
        context['body'] = editedArticleData['body']
        context['firstparagraph'],\
        context['secondparagraph'] = mediumSizePharagraphs(editedArticleData['body'])

        try:
            context['image1'] = getImages(1,slug)
        except:
            """Nothing"""

    elif len(wordcount) > 400:

        template = 'Layout_designer/long.html'
        context['wordcount'] = len(wordcount)
        context['body'] = editedArticleData['body']
        context['firstparagraph'], context['secondparagraph'], \
        context['thirdparagraph'] = largeSizePharagraphs(editedArticleData['body'])

        try:
            context['image1'], context['image2'] = getImages(2, slug)
        except:

            try:
                context['image1'] = getImages(1, slug)
            except:
                """Nothing"""

    return render(request,template,context)

def publishArticle(request):

    if request.method == "POST":

        dictionariRequest = request.POST.dict()


        publishedArticle = Published_Article()
        publishedArticle.slug = dictionariRequest['slug']
        publishedArticle.body = dictionariRequest['body']
        publishedArticle.title = dictionariRequest['title']
        publishedArticle.description = dictionariRequest['description']
        publishedArticle.save()


        return render(request,'Layout_designer/published_succesful.html')