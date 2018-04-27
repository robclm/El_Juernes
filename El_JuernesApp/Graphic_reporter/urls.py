from django.urls import path

from Graphic_reporter import views

urlpatterns = [
    path('noticies_assignades/', views.news_assigned, name="gr_assigned_news"),
    path('banc_imatges/', views.image_bank, name="gr_image_bank"),

]
