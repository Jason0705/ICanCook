from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings

from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add/$', views.add_recipe, name='add'),
    url(r'(?P<rid>[0-9]+)/edit/$', views.edit, name='edit'),
    url(r'(?P<rid>[0-9]+)/delete/$', views.delete, name='delete'),
    url(r'(?P<rid>[0-9]+)/remove/$', views.remove, name='remove'),
    url(r'(?P<rid>[0-9]+)/favourite/$', views.favourite, name='favourite'),
    url(r'(?P<rid>[0-9]+)/$', views.details, name='details'),
] 
