from django.http import HttpResponse
from django.shortcuts import render
from AfeNews.models import New
from Copywriter.models import Article


def getNewContext(slug):
    context = {}
    context['new'] = New.objects.get(slug=slug)
    context['article'] = Article.objects.get(slug=slug)
    return context

def news_assigned(request):
    template = 'Layout_designer/assigned_news.html'
    context = {'Acceptades': New.objects.filter(state="Acceptat")}

    return render(request, template, context)

def new_details(request,slug):
    context = getNewContext(slug)

    template = 'Layout_designer/layout_new.html'
    return render(request, template, context)



def maquetar(request,slug):
    context = getNewContext(slug)

    template = 'Layout_designer/layout_action.html'
    return render(request,template,context)



