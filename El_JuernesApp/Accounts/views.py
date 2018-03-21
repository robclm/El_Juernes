from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect

@login_required
def account_redirect(request):
    return redirect('account-landing', pk=request.user.pk, name=request.user.username)

@login_required
def AccountLanding(request, pk, name):
    return HttpResponse("Id: "+pk+" User: "+name)