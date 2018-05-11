from django.conf.urls import url
from django.urls import path

from Layout_designer import views

urlpatterns = [
    url(r'^layout/(?P<slug>[\w-]+)/$',views.maquetar,name ='maquetar'),
    url(r'^noticies_assignades/accepted/(?P<slug>[\w-]+)/$', views.new_details, name='new_layout'),
    path('noticies_assignades/', views.news_assigned, name="ld_assigned_news"),

]
