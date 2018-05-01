from django.conf.urls import url

from HeadCopywriter_ArticleValidation import views

urlpatterns = [
    url(r'^ArticlesPendents/$', views.Article_validation_list, name='Articles'),
    url(r'^validació/(?P<slug>[\w-]+)/$', views.Article_validation.as_view(), name='new_copywriter'),
    url(r'^Acceptat/$', views.Article_accepted, name='Acceptat'),
    url(r'^Comentat/$', views.Article_Comentat, name='Acceptat'),
]
