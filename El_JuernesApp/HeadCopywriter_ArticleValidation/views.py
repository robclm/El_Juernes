from django.contrib.auth.models import User
from django.shortcuts import render
from django.views import generic

from AfeNews.models import New


# Create your views here.


def Article_validation_list(request):
    template = 'Home_News.html'
    context = None
    try:
        user = User.objects.get(username=request.user.username)
        rol = user.user_profile.role
        if rol == "Head_copywriter":
            template = 'Head_copywriter/ArticlesToValidate.html'
        context = {
            "articles": New.objects.filter(tovalidate=True)
        }
    except:
        template = 'Home_News.html'

    return render(request, template, context)


class Article_validation(generic.DetailView):
    model = New
    context_object_name = 'new_head_copywriter'

    def get_context_data(self, **kwargs):
        context = super(Article_validation, self).get_context_data(**kwargs)
        context['new'] = New.objects.get(slug=self.kwargs['slug'])
        return context

    def get_template_names(self):
        template = 'Home_News.html'
        try:
            user = User.objects.get(username=self.request.user.username)
            rol = user.user_profile.role
            if rol == "Head_copywriter":
                template = 'Head_copywriter/ArticleValidation.html'
        except:
            template = 'Home_News.html'

        return template
