from django.conf.urls import url
from django.urls import path

from HeadCopywriter import views

urlpatterns = [
    url(r'^ArticlesPendents/$', views.Article_validation_list, name='Articles'),
    url(r'^validació/(?P<slug>[\w-]+)/$', views.Article_validation.as_view(), name='new_copywriter'),
    url(r'^Acceptat/$', views.Article_accepted, name='Acceptat'),
    url(r'^Comentat/$', views.Article_Comentat, name='Comentat'),
    url(r'^Rebutjat/$', views.Article_rejected, name='Rebutjada'),
    path('', views.home_page, name="hc_home_page"),
]
