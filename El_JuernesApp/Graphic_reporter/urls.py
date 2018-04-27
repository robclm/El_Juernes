from django.urls import path
from django.views.generic import TemplateView

from Graphic_reporter import views

urlpatterns = [
    path('noticies_assignades/', views.news_assigned, name="gr_assigned_news"),
    path('banc_imatges/', views.image_bank, name="gr_image_bank"),
    path('banc_imatges/pujar_imatges', views.upload_images, name="gr_upload_images"),

    path('banc_imatges/pujar_imatges/correcte',
         TemplateView.as_view(template_name="Graphic_reporter/correct_upload.html"),
         name="gr_correct_upload"),

]
