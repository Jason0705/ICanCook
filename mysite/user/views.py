from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views her.

LOGIN_URL = 'login/'


@login_required()
def index(request):
    return render(request, 'accounts/manage.html')


def login_page(request):
    next_url = request.GET.get('next', '/user/')
    context = {'next': next_url}
    return render(request, 'accounts/login.html', context)


@login_required()
def test(request):
    return render(request, 'accounts/test.html')


def login_user(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        url_next = request.POST.get('next', '/user/')

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)

                print(url_next)
                return HttpResponseRedirect(url_next)

    return HttpResponseRedirect(LOGIN_URL)
