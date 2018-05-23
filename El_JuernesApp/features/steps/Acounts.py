from behave import *

use_step_matcher("parse")


@given('Exists a HeadCoywriter "{HW}" with password "{password}"')
def step_impl(context, HW, password):
    from Accounts.models import User_profile
    from django.contrib.auth.models import User
    User.objects.create_user(username=HW, email='user@example.com', password=password)
    user = User.objects.get(username=HW)
    user_profile = User_profile()
    user_profile.user = user
    user_profile.role = "Head_copywriter"
    user_profile.save()


@given('Exists a Coywriter "{CW}" with password "{password}"')
def step_impl(context, CW, password):
    from Accounts.models import User_profile
    from django.contrib.auth.models import User
    User.objects.create_user(username=CW, email='user@example.com', password=password)
    user = User.objects.get(username=CW)
    user_profile = User_profile()
    user_profile.user = user
    user_profile.role = "Copywriter"
    user_profile.save()
