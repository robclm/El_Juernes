from django.conf.urls import url
from django.urls import path
from django.views.generic import TemplateView

from Copywriter import views

urlpatterns = [

    url(r'^request_send/$', views.send_request, name='request_send'),
    url(r'^send_article/$', views.send_new, name='send'),
    url(r'^assigned/(?P<slug>[\w-]+)/$', views.new_copywriter.as_view(), name='new_copywriter'),
    path('', views.News_assigned, name="assigned"),

    path('article_enviat/',
         TemplateView.as_view(template_name="Copywriter/correct_send.html"),
         name="cw_correct_send_article"),


]
