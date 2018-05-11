from django.conf.urls import url
from django.urls import path

from Copywriter import views

urlpatterns = [

    url(r'^request_send/$', views.send_request, name='request_send'),
    url(r'^send_article/$', views.send_new, name='send'),
    url(r'^assigned/(?P<slug>[\w-]+)/$', views.new_copywriter.as_view(), name='new_copywriter'),
    url(r'^Revisions/(?P<slug>[\w-]+)/$', views.Review_new.as_view(), name='review_new'),
    url(r'^Revisions/$', views.News_review, name='revisions'),
    path('', views.News_assigned, name="assigned"),

]
