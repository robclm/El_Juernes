from django.urls import path

from AfeNews.views import Afe_News_List

urlpatterns = [
    path('', Afe_News_List, name="AFE"),

]
