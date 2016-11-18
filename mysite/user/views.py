from django.contrib.auth import authenticate, login as dlogin, logout as dlogout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views her.
from user.forms import LoginForm


@login_required()
def index(request):
    c = {'user': request.user}
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
    current_user = request.user

    first_name = request.POST.get('firstname', current_user.first_name)
    last_name = request.POST.get('lastname', current_user.last_name)
    email = request.POST.get('email', current_user.email)

    if not first_name:
        pass  # Return empty first name error

    if not last_name:
        pass  # Return empty last name error

    if not email:
        pass  # Return empty email error

    current_user.first_name = first_name
    current_user.last_name = last_name
    current_user.email = email
    current_user.save()

    c = {'user': current_user}
    return render(request, 'accounts/manage.html', c)


def logout(request):
    dlogout(request)
    return HttpResponseRedirect('/user/')
