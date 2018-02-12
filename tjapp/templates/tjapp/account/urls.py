from django.conf.urls import url
from django.contrib.auth.views import login, logout, logout_then_login
from . import views

urlpatterns = [

    # url(r'^login/$', views.user_login, name='login'),

    # login / logout urls
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^logout-then-login/$', logout_then_login, name='logout_then_login'),

    # Register
    url(r'^register/$', views.register, name='register'),

    url(r'^$', views.dashboard, name='dashboard'),
]
