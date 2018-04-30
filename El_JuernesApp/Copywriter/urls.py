from Copywriter import views
from django.conf.urls import url
from django.urls import path

urlpatterns = [
    path('', views.News_assigned, name="assigned"),
    url(r'^assigned/(?P<slug>[\w-]+)/$', views.new_copywriter.as_view(), name='new_copywriter'),
    path('images/', views.Image_management, name="Image_management"),
    url('(?P<slug>[\w-]+)/$', views.images_copywriter.as_view(), name='image_copywriter'),
]
