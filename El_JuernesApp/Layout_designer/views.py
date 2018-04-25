from django.shortcuts import render


def news_assigned(request):
    template = 'Layout_designer/assigned_news.html'
    context = None

    return render(request, template, context)
