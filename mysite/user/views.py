from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views her.

LOGIN_URL = 'login/'


@login_required(login_url=LOGIN_URL)
def index(request):
    return render(request, 'accounts/manage.html')


def login_page(request):
    return render(request, 'accounts/login.html')


def login_user(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/user/')

    return HttpResponseRedirect(LOGIN_URL)
