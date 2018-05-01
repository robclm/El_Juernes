from HeadCopywriter_ArticleValidation import views
from django.conf.urls import url

urlpatterns = [
    url(r'^ArticlesPendents/$', views.Article_validation_list, name='Articles'),
    url(r'^validació/(?P<slug>[\w-]+)/$', views.Article_validation.as_view(), name='new_copywriter'),
    url(r'^Acceptat/$', views.Article_accepted, name='Acceptat'),
]
