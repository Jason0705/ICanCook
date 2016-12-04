from django.contrib.auth import authenticate, login as dlogin, logout as dlogout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.db import IntegrityError

# Create your views her.
from recipes.models import Recipe
from user.forms import LoginForm, UpdateUserForm, UpdatePasswordForm, UserForm

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
            form = UserForm(request.POST)

            if form.is_valid():
                user = form.save()
                user.first_name = form.cleaned_data['first_name']
                user.last_name = form.cleaned_data['last_name']
                user.username = form.cleaned_data['username']
                user.email = form.cleaned_data['email']
                user.password = form.cleaned_data['password']
                user.password_confirm = form.cleaned_data['password_confirm']
                user.set_password(user.password)
                user.save()

                return HttpResponseRedirect('/user/login')
            else:
                form.add_error(None, "Please enter all fields correctly")

        except IntegrityError:
            form.add_error(None, "Username is already taken")
            return render(request, 'accounts/create.html', {'form': form})
    else:
        form = UserForm()

    return render(request, 'accounts/create.html', {'form': form})


@login_required()
def recipes(request):
    user_id = request.user.id
    my_recipes = Recipe.objects.filter(userid=user_id)
    return render(request, 'accounts/my_recipes.html', {'recipes': my_recipes})

@login_required()
def favourites(request):
    user_id = request.user.id
    favourited_recipes = Recipe.objects.filter(favourites=user_id)
    return render(request, 'accounts/favourites.html', {'recipes': favourited_recipes})


@login_required()
def update(request):
    if request.POST:
        form = UpdateUserForm(request.POST)

        if form.is_valid():
            current_user = request.user

            #current_user.profile_pic = form.cleaned_data['profile_pic']
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
