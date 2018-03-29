from django.conf.urls import url
from django.urls import path

from AfeNews import views
from AfeNews.views import Afe_News_List

urlpatterns = [
    path('', Afe_News_List, name="AFE"),
    url(r'^new/(?P<slug>[\w-]+)/$', views.full_new_and_assignations.as_view(), name='full_new_and_assignations')
]
