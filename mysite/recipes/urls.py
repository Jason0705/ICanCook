from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings

from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add/$', views.add_recipe, name='add'),
    url(r'^quick/$', views.quick, name='quick'),
    url(r'^tips/$', views.tips, name='tips'),
    url(r'^lowcal/$', views.lowcal, name='lowcal'),
    url(r'^healthy_living/$', views.healthy_living, name='healthy_living'),
    url(r'^nutrition_guide/$', views.nutrition_guide, name='nutrition_guide'),
    url(r'^breakfast/$', views.breakfast, name='breakfast'),
    url(r'^lunch/$', views.lunch, name='lunch'),
    url(r'^dinner/$', views.dinner, name='dinner'),
    url(r'^dessert/$', views.dessert, name='dessert'),
    url(r'^holiday/$', views.holiday, name='holiday'),
    url(r'(?P<rid>[0-9]+)/edit/$', views.edit, name='edit'),
    url(r'(?P<rid>[0-9]+)/delete/$', views.delete, name='delete'),
    url(r'(?P<rid>[0-9]+)/remove/$', views.remove, name='remove'),
    url(r'(?P<rid>[0-9]+)/favourite/$', views.favourite, name='favourite'),
    url(r'(?P<rid>[0-9]+)/$', views.details, name='details'),
]
