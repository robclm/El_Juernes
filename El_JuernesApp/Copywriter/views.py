from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.shortcuts import render
from django.views import generic

from AfeNews.models import New
from Copywriter.models import Article


# Create your views here.

def News_assigned(request):
    template = 'Home_News.html'
    context = None
    try:
        user = User.objects.get(username=request.user.username)
        rol = user.user_profile.role
        if rol == "Copywriter":
            if request.method == 'POST':
                var = request.POST.dict()
                title = var['title']
                description = var['description']
                body = var['body']
                name = var['new'].split('/')
                new_obj = New.objects.get(slug=name[0])
                new_obj.tovalidate = True
                new_obj.save()

                article = Article()
                article.slug = name[0]
                article.title = title
                article.description = description
                article.body = body
                article.assigned = new_obj.assigned
                article.priority = new_obj.priority
                article.save()

                template = 'http://127.0.0.1:8000/accounts'
                return redirect(template)

            template = 'Copywriter/AssignedNewsList.html'
        context = {
            "articles": New.objects.filter(assigned=request.user.username)
        }
    except:
        template = 'Home_News.html'

    return render(request, template, context)


class new_copywriter(generic.DetailView):
    model = New
    context_object_name = 'new_copywriter'

    def get_context_data(self, **kwargs):
        context = super(new_copywriter, self).get_context_data(**kwargs)
        context['new'] = New.objects.get(slug=self.kwargs['slug'])
        return context

    def get_template_names(self):
        template = 'Home_News.html'
        try:
            user = User.objects.get(username=self.request.user.username)
            rol = user.user_profile.role
            if rol == "Copywriter":
                template = 'Copywriter/New_Copywriter.html'
        except:
            template = 'Home_News.html'

        return template
