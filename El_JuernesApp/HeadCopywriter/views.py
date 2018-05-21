from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.utils import timezone
from django.views import generic

from Accounts.models import User_profile
from AfeNews.models import New
from Copywriter.models import Article
from Graphic_reporter.models import Image
from HeadCopywriter.forms import ArticleComentatForm
from HeadCopywriter.models import Article_comentat, Images_sended


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
            "articles_alta": New.objects.filter(state="Per validar", priority='alta'),
            "articles_mitjana": New.objects.filter(state="Per validar", priority='mitjana'),
            "articles_baixa": New.objects.filter(state="Per validar", priority='baixa'),
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
        context['article'] = Article.objects.get(slug=self.kwargs['slug'])
        context['form'] = ArticleComentatForm()
        context['images'] = Images_sended.objects.get(slug=self.kwargs['slug']).images.all()


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


# Article acceptat

def Article_accepted(request):
    template = 'Home_News.html'
    selected_images_pk = request.POST.getlist('selected_image')

    try:
        user = User.objects.get(username=request.user.username)
        rol = user.user_profile.role
        if rol == "Head_copywriter":
            template = 'Head_copywriter/Correct_Validation.html'
    except Exception as e:
        print("%s (%s)" % (e.args, type(e)))

    if request.method == 'POST':
        var = request.POST.dict()
        name = var['slug'].split('/')

        new = New.objects.get(slug=name[0])
        new.state = "Acceptat"
        new.save()

        article = Article.objects.get(slug=name[0])
        for pk in selected_images_pk:
            image = Image.objects.get(pk=pk)
            article.images.add(image)

    return render(request, template)


# Article comentat

def Article_Comentat(request):
    template = 'Home_News.html'

    try:
        user = User.objects.get(username=request.user.username)
        rol = user.user_profile.role
        if rol == "Head_copywriter":
            template = 'Head_copywriter/Correct_Validation.html'
    except Exception as e:
        print("%s (%s)" % (e.args, type(e)))

    if request.method == 'POST':
        form = ArticleComentatForm(request.POST or None, request.FILES or None)

        if form.is_valid():
            var = request.POST.dict()
            articleComentat = Article_comentat()
            articleComentat.file = form.clean_file()
            articleComentat.slug = var['slug']
            articleComentat.save()

            new = New.objects.get(slug=var['slug'])
            new.state = "Comentat"
            new.save()

    return render(request, template)


# Article denegat
def Article_rejected(request):
    template = 'Home_News.html'

    try:
        user = User.objects.get(username=request.user.username)
        rol = user.user_profile.role
        if rol == "Head_copywriter":
            template = 'Head_copywriter/Correct_Validation.html'
    except Exception as e:
        print("%s (%s)" % (e.args, type(e)))

    if request.method == 'POST':
        var = request.POST.dict()
        name = var['slug'].split('/')

        new = New.objects.get(slug=name[0])
        new.state = "Rebutjada"
        new.save()

    return render(request, template)


def role_is_head_copywriter(username):
    # Check if the user is a copywriter
    user = User.objects.get(username=username)

    if user.user_profile.role == "Head_copywriter":
        return True
    else:
        return False



def countdown_format(countdown):
    # Eliminate microseconds
    countdown = countdown[:countdown.rfind(".")]

    # Days in catalan
    countdown = countdown.replace("days", "dies")
    countdown = countdown.replace("day", "dia")

    return countdown


def update_countdown(assigned_news):
    for new in assigned_news:
        countdown = new.limit_date - timezone.now()
        new.countdown = countdown_format(str(countdown))
        new.save()

    return assigned_news

@login_required(login_url='/accounts/login')
def home_page(request):
    if not role_is_head_copywriter(request.user.username):
        return redirect('access_denied')

    template = 'Head_copywriter/home.html'

    assigned_news = New.objects.all()
    assigned_news = assigned_news.filter(state='Assignada')
    assigned_news = assigned_news.order_by('limit_date')[:5]
    assigned_news = update_countdown(assigned_news)

    return render(request, template, {'assigned_news': assigned_news})

@login_required(login_url='/accounts/login')
def work_load(request):
    if not role_is_head_copywriter(request.user.username):
        return redirect('access_denied')

    assigned_news = New.objects.all()
    assigned_news = assigned_news.filter(state='Assignada')
    assigned_news = assigned_news.order_by('assigned')
    copywriters  = User_profile.objects.filter(role='Copywriter')



    template = 'Head_copywriter/work_load.html'
    return render(request, template, {'assigned_news': assigned_news,
                                      'copywriters': copywriters})