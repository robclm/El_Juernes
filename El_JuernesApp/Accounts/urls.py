from django.conf.urls import url
from django.urls import path, include
from Accounts.views import account_redirect, AccountLanding


urlpatterns = [
    url(r'^(?P<pk>\d+)/(?P<name>\w+)/$', AccountLanding, name="account-landing"),
    url(r'^$', account_redirect, name='account-redirect'),
    path('', include('django.contrib.auth.urls')),
]