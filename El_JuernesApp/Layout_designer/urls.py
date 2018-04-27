from django.urls import path

from Layout_designer import views

urlpatterns = [
    path('noticies_assignades/', views.news_assigned, name="ld_assigned_news"),

]
