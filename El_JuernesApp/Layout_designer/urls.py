from django.conf.urls import url
from django.urls import path
from django.views.generic import TemplateView

from Layout_designer import views

urlpatterns = [
    url(r'^published/$',views.publishArticle,name ='published'),
    url(r'^preview/(?P<slug>[\w-]+)/$',views.preview,name ='preview'),
    url(r'^layout/(?P<slug>[\w-]+)/$',views.maquetar,name ='maquetar'),
    url(r'^noticies_assignades/accepted/(?P<slug>[\w-]+)/$', views.new_details, name='new_layout'),
    path('noticies_assignades/', views.news_assigned, name="ld_assigned_news"),

]
