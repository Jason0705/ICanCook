from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse("Hello, world. You're at the accounts index.")


def test(request, id):
    return HttpResponse("Argument is: " + id)
