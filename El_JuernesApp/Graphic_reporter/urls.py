from django.urls import path
from django.views.generic import TemplateView

from Graphic_reporter import views

urlpatterns = [
    path('noticies_assignades/', views.news_assigned, name="gr_assigned_news"),
    path('banc_imatges/', views.image_bank, name="gr_image_bank"),
    path('banc_imatges/pujar_imatge', views.upload_image, name="gr_upload_image"),

    path('banc_imatges/pujar_imatge/pujar_correcte',
         TemplateView.as_view(template_name="Graphic_reporter/correct_upload.html"),
         name="gr_correct_upload"),

    path('banc_imatges/pujar_imatge/editar_correcte',
         TemplateView.as_view(template_name="Graphic_reporter/correct_edit.html"),
         name="gr_correct_edit"),

    path('banc_imatges/editar_imatge/<int:pk>', views.edit_image, name="gr_edit_image"),

    path('noticies_assignades/noticia/<int:pk>', views.images_new_request, name="gr_images_new_request"),

    path('noticies_assignades/noticia/<int:pk>/seleccionar_imatges/',
         views.select_images, name="gr_select_images"),

]
