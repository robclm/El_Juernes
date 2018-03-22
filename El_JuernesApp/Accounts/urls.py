from django.conf.urls import url
from django.contrib.auth.models import User
from django.urls import path, include
from django.views.generic import DetailView

from Accounts.views import account_redirect

urlpatterns = [
    url(r'^(?P<pk>\d+)/(?P<name>\w+)/$',
        DetailView.as_view(
            model=User,
            template_name='home.html'),
        name="account-landing"),
    url(r'^$', account_redirect, name='account-redirect'),
    path('', include('django.contrib.auth.urls')),
]