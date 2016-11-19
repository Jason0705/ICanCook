from django.contrib.auth import authenticate, login as dlogin, logout as dlogout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views her.
from user.forms import LoginForm, UpdateUserForm


@login_required()
def index(request):
    form = UpdateUserForm()

    u = request.user
    form.initial = {'user': u, 'first_name': u.first_name, 'last_name': u.last_name, 'email': u.email}

    c = {'username': u.username, 'form': form}
    return render(request, 'accounts/manage.html', c)


def login(request):
    if request.POST:
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            url_next = form.cleaned_data['next']

            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    dlogin(request, user)
                    return HttpResponseRedirect(url_next)
            else:
                form.add_error(None, "The username and password are not valid.")

    else:
        next_url = request.GET.get('next', '/user/')
        form = LoginForm(initial={'next': next_url})

    return render(request, 'accounts/login.html', {'form': form})


def signup(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']

        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')

        user = User.objects.create_user(username, email, password)
        user.first_name = first_name
        user.last_name = last_name
        user.set_password(user.password)
        user.save()
        return HttpResponseRedirect('/user/login')
    else:
        return render(request, 'accounts/create.html')


@login_required()
def test(request):
    return render(request, 'accounts/test.html')


@login_required()
def update_user(request):
    if request.POST:
        form = UpdateUserForm(request.POST)

        if form.is_valid():
            current_user = request.user

            current_user.first_name = form.cleaned_data['first_name']
            current_user.last_name = form.cleaned_data['last_name']
            current_user.email = form.cleaned_data['email']
            current_user.save()
        else:
            return render(request, 'accounts/manage.html', {'user': request.user, 'form': form})

    return HttpResponseRedirect('/user/')


def logout(request):
    dlogout(request)
    return HttpResponseRedirect('/user/')
