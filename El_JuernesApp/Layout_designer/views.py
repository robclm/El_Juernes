from django.http import HttpResponse
from django.shortcuts import render
from AfeNews.models import New
from Copywriter.models import Article


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
    var = request.POST.dict()
    toParse = var['body']
    wordcount = toParse.split(" ")
    context = {}
    template = ""
    if len(wordcount) <= 100:
        template = 'Layout_designer/short.html'
        context['wordcount'] = len(wordcount)
    elif 100 < len(wordcount) <= 400:
        template = 'Layout_designer/medium.html'
        context['wordcount'] = len(wordcount)
    elif len(wordcount) > 400:
        template = 'Layout_designer/long.html'
        context['wordcount'] = len(wordcount)

    return render(request,template,context)
