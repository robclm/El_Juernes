from django.contrib.auth.models import User
from django.shortcuts import render
from django.utils import timezone
from django.views import generic
from Layout_designer.models import Published_Article



def home(request):

    published = Published_Article.objects.all()
    context = {'published': published}

    return render(request,'Home_News.html',context)