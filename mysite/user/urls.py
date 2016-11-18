from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.login, name='login'),
    url(r'^login_user/$', views.login_user, name='login_user'),
    url(r'^logout_user/$', views.logout_user, name='logout_user'),
    url(r'^update_user/$', views.update_user, name='update_user'),
    url(r'^test/$', views.test, name='test'),
    url(r'^signup/$', views.signup, name='signup')
]
