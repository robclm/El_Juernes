from django.http import HttpResponse
from django.template.loader import get_template


def Afe_News_List(request):
    template = get_template("AfeNews/AfeNewsList.html")
    data = {"articles": [
        {"slug": "lorem-ipsum-tbeoud", "title": "Lorem ipsum", "description": "This is a test with Lorem ipsum",
         "body": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
         "type": {"name": "National", "description": "National news"},
         "author": {"username": "user1", "image": "https://static.productionready.io/images/smiley-cyrus.jpg"}},
        {"slug": "trump-desafia-a-kim-jong-a-un-torneig-de-fortnite-o9bn1h",
         "title": "Trump desafia a Kim Jong a un torneig de Fortnite",
         "description": "El desafiament preten evitar una escalada nuclear",
         "body": "Per tal d'evitar un conflicte nuclear entre les dos potencies, Trump ha proposat arreglar les seves diferencies a través del famós joc de playstation. El guanyador es quedarà amb el país del altre i el perdedor haurà de pagar per el manteniment del servidor que utilitzi el seu vencedor per a jugar. \nD'aquesta forma s'espera evitar milions de morts i una escalada nuclear, arreglant les seves diferencies civilitzadament. ",
         "type": {"name": "International", "description": "International news"},
         "author": {"username": "gr5", "image": "https://static.productionready.io/images/smiley-cyrus.jpg"}}],
        "articlesCount": 2}

    output = template.render(data)
    return HttpResponse(output)
