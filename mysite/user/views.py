from django.contrib.auth import authenticate, login as dlogin, logout as dlogout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User
from django.db import IntegrityError

# Create your views her.
from recipes.models import Recipe
from user.forms import LoginForm, UpdateUserForm, UpdatePasswordForm

PASSWORD_FORM = 'password_form'

INFO_FORM = 'info_form'


def get_index_base_context(request):
    u = request.user
    info_form = UpdateUserForm()
    info_form.initial = {'user': u, 'first_name': u.first_name, 'last_name': u.last_name, 'email': u.email}

    password_form = UpdatePasswordForm(username=request.user.username)

    c = {'username': u.username, INFO_FORM: info_form, PASSWORD_FORM: password_form}
    return c


@login_required()
def index(request):
    return render(request, 'accounts/manage.html', get_index_base_context(request))


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
        try:
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
        except IntegrityError:
            return render(request, 'accounts/create.html')
        return HttpResponseRedirect('/user/login')
    else:
        return render(request, 'accounts/create.html')


@login_required()
def recipes(request):
    user_id = request.user.id
    my_recipes = Recipe.objects.filter(userid=user_id)
    return render(request, 'accounts/my_recipes.html', {'recipes': my_recipes})


@login_required()
def update(request):
    if request.POST:
        form = UpdateUserForm(request.POST)

        if form.is_valid():
            current_user = request.user

            current_user.first_name = form.cleaned_data['first_name']
            current_user.last_name = form.cleaned_data['last_name']
            current_user.email = form.cleaned_data['email']
            current_user.save()
        else:
            c = get_index_base_context(request)
            c[INFO_FORM] = form
            return render(request, 'accounts/manage.html', c)

    return HttpResponseRedirect('/user/')


@login_required()
def update_password(request):
    if request.POST:
        form = UpdatePasswordForm(request.POST, username=request.user.username)

        if form.is_valid():
            current_user = request.user
            current_user.set_password(form.cleaned_data['new_password'])
            current_user.save()
        else:
            c = get_index_base_context(request)
            c[PASSWORD_FORM] = form
            return render(request, 'accounts/manage.html', c)

    return HttpResponseRedirect('/user/')


def logout(request):
    next_url = request.GET.get('next', '/user/')

    dlogout(request)
    return HttpResponseRedirect(next_url)
