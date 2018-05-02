from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.shortcuts import render
from django.views import generic

from AfeNews.models import New
from Copywriter.forms import ArticleForm
from Copywriter.models import Article


# Create your views here.

def News_assigned(request):
    template = 'Home_News.html'
    context = None
    try:
        user = User.objects.get(username=request.user.username)
        rol = user.user_profile.role
        if rol == "Copywriter":
            template = 'Copywriter/AssignedNewsList.html'
        context = {
            "articles_alta": New.objects.filter(assigned=request.user.username, priority='alta'),
            "articles_mitjana": New.objects.filter(assigned=request.user.username, priority='mitjana'),
            "articles_baixa": New.objects.filter(assigned=request.user.username, priority='baixa')
        }
    except Exception as e:
        print("%s (%s)" % (e.args, type(e)))

    return render(request, template, context)



def send_request(request):
    template = 'Copywriter/correct_request.html'
    return render(request,template)

def send_new(request):
    template = 'http://127.0.0.1:8000'

    try:
        user = User.objects.get(username=request.user.username)
        rol = user.user_profile.role
        if rol == "Copywriter":
            template = 'Copywriter/New_Copywriter.html'
    except Exception as e:
        print("%s (%s)" % (e.args, type(e)))

    if request.method == 'POST':
        form = ArticleForm(request.POST or None, request.FILES or None)

        if form.is_valid():
            var = request.POST.dict()
            article = Article()
            article.file = form.clean_file()
            article.slug = var['slug']
            article.save()

            new=New.objects.get(slug=var['slug'])
            new.tovalidate = True
            new.save()

        template = 'http://127.0.0.1:8000/accounts'

    return redirect(template)



class new_copywriter(generic.DetailView):
    model = New
    context_object_name = 'new_copywriter'

    def get_context_data(self, **kwargs):
        context = super(new_copywriter, self).get_context_data(**kwargs)
        context['new'] = New.objects.get(slug=self.kwargs['slug'])
        context['form'] = ArticleForm()
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
