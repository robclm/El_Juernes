from django.conf.urls import url

from HeadCopywriter_ArticleValidation import views

urlpatterns = [
    url(r'^ArticlesPendents/$', views.Article_validation, name='Articles'),
]
