from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^update/$', views.update, name='update'),
    url(r'^test/$', views.test, name='test'),
    url(r'^signup/$', views.signup, name='signup')
]
