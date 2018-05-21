from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.shortcuts import render
from django.utils import timezone
from django.views import generic

from AfeNews.models import New
from Copywriter.forms import ArticleForm
from Copywriter.models import Article
from Graphic_reporter.models import Image_request, Image
from HeadCopywriter.models import Article_comentat, Images_sended


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
            "articles_alta": New.objects.filter(assigned=request.user.username, priority='alta', state="Assignada"),
            "articles_mitjana": New.objects.filter(assigned=request.user.username, priority='mitjana',
                                                   state="Assignada"),
            "articles_baixa": New.objects.filter(assigned=request.user.username, priority='baixa', state="Assignada")
        }
    except Exception as e:
        print("%s (%s)" % (e.args, type(e)))

    return render(request, template, context)

##############################################################################
def priority_news(request):
    template = 'Accounts/Home/home.html'
    user = User.objects.get(username=request.user.username)
    rol = user.user_profile.role
    new = News_assigned()
    context = {
        "articles_alta": New.objects.filter(assigned=request.user.username, value="1")
    }
    return render(request, template, context)

###############################################################################

def send_request(request):
    template = 'Copywriter/correct_request.html'

    var = request.POST.dict()
    new = New.objects.get(slug=var['slug'])
    context = {}
    image_request = Image_request()
    try:
        found = Image_request.objects.get(noticia=new)
    except Image_request.DoesNotExist:
        found = None

    if found is not None:
        context['found'] = "Una petició feta amb anterioritat ha estat actualitzada"
        found.comment = var["body"]
        found.save()

    else:
        context['found'] = "La petició ha estat enviada correctament"
        image_request.noticia = new
        image_request.state = "To do"
        image_request.comment = var["body"]
        image_request.save()

    return render(request, template, context)


def role_is_copywriter(username):
    # Check if the user is a copywriter
    user = User.objects.get(username=username)

    if user.user_profile.role == "Copywriter":
        return True
    else:
        return False


@login_required(login_url='/accounts/login')
def send_new(request):

    # Check if the role is correct
    if not role_is_copywriter(request.user.username):
        return redirect('access_denied')

    template = 'Copywriter/New_Copywriter.html'

    # Submit an Article
    if request.method == 'POST':
        form = ArticleForm(request.POST or None, request.FILES or None)
        selected_images_pk = request.POST.getlist('selected_image')

        if form.is_valid():
            var = request.POST.dict()
            try:
                article = Article.objects.get(slug=var['slug'])
                article.file = form.clean_file()
                # Must be saved before adding the images
                article.save()
            except:
                article = Article()
                article.slug = var['slug']
                article.file = form.clean_file()
                # Must be saved before adding the images
                article.save()

            images_sended = Images_sended()
            images_sended.slug = var['slug']
            images_sended.save()

            for pk in selected_images_pk:
                image = Image.objects.get(pk=pk)
                images_sended.images.add(image)

            images_sended.save()

            new = New.objects.get(slug=var['slug'])
            new.state = "Per validar"
            new.save()
            context = {
                "article": article,
                "new": new,
            }

            return render(request, 'Copywriter/correct_send.html', context)

    return redirect('new_copywriter')


class new_copywriter(generic.DetailView):
    model = New
    context_object_name = 'new_copywriter'

    def get_context_data(self, **kwargs):
        context = super(new_copywriter, self).get_context_data(**kwargs)
        context['new'] = New.objects.get(slug=self.kwargs['slug'])
        context['form'] = ArticleForm()

        try:
            context['image_request'] = Image_request.objects.get(noticia=context['new'])

            if context['image_request'].state == 'Send':
                context['images'] = context['image_request'].images.all()

        except Exception as e:
            print("%s (%s)" % (e.args, type(e)))

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


def News_review(request):
    template = 'Home_News.html'
    context = None
    try:
        user = User.objects.get(username=request.user.username)
        rol = user.user_profile.role
        if rol == "Copywriter":
            template = 'Copywriter/ReviewNewsList.html'
        context = {
            "articles_alta": New.objects.filter(assigned=request.user.username, priority='alta', state="Comentat"),
            "articles_mitjana": New.objects.filter(assigned=request.user.username, priority='mitjana',
                                                   state="Comentat"),
            "articles_baixa": New.objects.filter(assigned=request.user.username, priority='baixa', state="Comentat")
        }
    except Exception as e:
        print("%s (%s)" % (e.args, type(e)))

    return render(request, template, context)


class Review_new(generic.DetailView):
    model = New
    context_object_name = 'Review_new'

    def get_context_data(self, **kwargs):
        context = super(Review_new, self).get_context_data(**kwargs)
        context['new'] = New.objects.get(slug=self.kwargs['slug'])
        context['article'] = Article_comentat.objects.get(slug=self.kwargs['slug'])
        return context

    def get_template_names(self):
        template = 'Home_News.html'
        try:
            user = User.objects.get(username=self.request.user.username)
            rol = user.user_profile.role
            if rol == "Copywriter":
                template = 'Copywriter/ReviewNew.html'
        except:
            template = 'Home_News.html'

        return template

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
def Home(request):
    if not role_is_copywriter(request.user.username):
        return redirect('access_denied')
    template = 'Copywriter/home.html'

    assigned_news = New.objects.all()
    assigned_news = assigned_news.filter(state='Assignada', assigned=request.user.username)
    num_assigned_news = assigned_news.count()

    assigned_news = assigned_news.order_by('limit_date')[:5]
    assigned_news = update_countdown(assigned_news)

    return render(request, template, {'assigned_news': assigned_news,
                                      'num_assigned_news': num_assigned_news})