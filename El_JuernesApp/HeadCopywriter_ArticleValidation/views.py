from django.contrib.auth.models import User
from django.shortcuts import render

from AfeNews.models import New


# Create your views here.
def Article_validation(request):
    template = 'Home_News.html'
    context = None
    try:
        user = User.objects.get(username=request.user.username)
        rol = user.user_profile.role
        if rol == "Head_copywriter":
            template = 'Head_copywriter/ArticlesToValidate.html'
        context = {
            "articles": New.objects.filter()
        }
    except:
        template = 'Home_News.html'

    return render(request, template, context)
