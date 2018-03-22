import json
from urllib.request import urlopen

from AfeNews.models import New, Author
from django.http import HttpResponse
from django.template.loader import get_template


def Afe_News_List(request):
    template = get_template("AfeNews/AfeNewsList.html")
    json_data = get_json_AFE_news()

    output = template.render(json_data)
    return HttpResponse(output)


def get_json_AFE_news():
    json_obj = urlopen("http://enigmatic-waters-71955.herokuapp.com/api/news")
    json_data = json.load(json_obj)

    save_news_to_db(json_data)

    return json_data


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
