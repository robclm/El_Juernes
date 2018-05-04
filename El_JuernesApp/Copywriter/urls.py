from django.conf.urls import url
from django.urls import path

from Copywriter import views

urlpatterns = [

    url(r'^request_send/$', views.send_request, name='request_send'),
    url(r'^send_article/$', views.send_new, name='send'),
    url(r'^assigned/(?P<slug>[\w-]+)/$', views.new_copywriter.as_view(), name='new_copywriter'),
    path('', views.News_assigned, name="assigned"),

]
