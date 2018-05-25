from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect, render


@login_required
def account_redirect(request):
    return redirect('account-landing', pk=request.user.pk, name=request.user.username)


def Home(request, pk, name):
    template = 'Home_News.html'
    try:
        user = User.objects.get(username=request.user.username)
        rol = user.user_profile.role

        if rol == "Subscriber":
            return redirect('Home_News')

        elif rol == "Copywriter":
            return redirect('cw_home_page')

        elif rol == "Head_copywriter":
            return redirect('hc_home_page')

        elif rol == "Graphic_reporter":
            template = 'Accounts/Home/graphic_reporter.html'
        elif rol == "Layout_designer":
            return redirect('ld_home')
    except:
        template = 'Home_News.html'

    return render(request, template)
