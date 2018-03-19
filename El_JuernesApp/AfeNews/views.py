import json
from urllib.request import urlopen

from django.http import HttpResponse
from django.template.loader import get_template


def Afe_News_List(request):
    template = get_template("AfeNews/AfeNewsList.html")

    json_obj = urlopen("http://enigmatic-waters-71955.herokuapp.com/api/news")
    json_data = json.load(json_obj)

    output = template.render(json_data)
    return HttpResponse(output)
