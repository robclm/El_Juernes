import codecs
import json
from urllib.request import urlopen

from django.contrib.auth.models import User
from django.shortcuts import render
from django.utils import timezone
from django.views import generic

from Accounts.models import User_profile
from AfeNews.models import New, Author


def set_limit_date(priority):
    if priority == 'alta':
        limit = timezone.now() + timezone.timedelta(hours=1)

    elif priority == 'mitjana':
        limit = timezone.now() + timezone.timedelta(days=1)

    else:
        limit = timezone.now() + timezone.timedelta(days=30)

    return limit


def Afe_News_List(request):
    context = None
    # Assignar notícia
    if request.method == 'POST':
        var = request.POST.dict()
        name = var['new'].split('/')
        writer = var['copywriters']
        prioritat = var['priority']
        new_obj = New.objects.get(slug=name[0])
        user = User.objects.get(username=writer)
        new_obj.assigned = user.username
        new_obj.priority = prioritat
        new_obj.state = "Assignada"

        new_obj.limit_date = set_limit_date(new_obj.priority)

        new_obj.save()

        template = 'Head_copywriter/Correct_Assigned.html'
        context = {
            "new": New.objects.get(slug=name[0])
        }
        return render(request, template, context)

    else:
        template = 'Home_News.html'
        json_data = None

        try:
            user = User.objects.get(username=request.user.username)
            rol = user.user_profile.role

            if rol == "Head_copywriter":
                template = 'AfeNews/AfeNewsList.html'

            context = {
                "articles": get_json_AFE_news(),
            }
        except:
            template = 'Home_News.html'

        return render(request, template, context)


def get_json_AFE_news():
    json_obj = urlopen("http://enigmatic-waters-71955.herokuapp.com/api/news")
    reader = codecs.getreader("utf-8")
    json_data = json.load(reader(json_obj))
    save_news_to_db(json_data)
    new = New.objects.filter(state="Nova notícia")

    return new


def save_news_to_db(json_data):
    for i in range(0, json_data["articlesCount"]):

        try:
            new_obj = New.objects.get(slug=json_data["articles"][i]["slug"])

        except New.DoesNotExist:
            new = New()

            new.slug = json_data["articles"][i]["slug"]
            new.title = json_data["articles"][i]["title"]
            new.description = json_data["articles"][i]["description"]
            new.body = json_data["articles"][i]["body"]
            new.type = json_data["articles"][i]["type"]["name"]

            try:
                author = Author.objects.get(username=json_data["articles"][i]["author"]["username"])

            except Author.DoesNotExist:
                author = Author()

                author.username = json_data["articles"][i]["author"]["username"]
                author.image = json_data["articles"][i]["author"]["image"]

                author.save()

            new.author = author
            new.save()


class full_new_and_assignations(generic.DetailView):
    model = New
    context_object_name = 'new_and_assignation'

    def get_context_data(self, **kwargs):
        context = super(full_new_and_assignations, self).get_context_data(**kwargs)
        context['redactors'] = User_profile.objects.filter(role='Copywriter')
        context['new'] = New.objects.get(slug=self.kwargs['slug'])
        return context

    def get_template_names(self):
        template = 'Home_News.html'
        try:
            user = User.objects.get(username=self.request.user.username)
            rol = user.user_profile.role
            if rol == "Head_copywriter":
                template = 'AfeNews/New.html'
        except:
            template = 'Home_News.html'

        return template
