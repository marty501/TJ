from django.conf.urls import url, include
from . import views


urlpatterns = [
    # url(r'^$', views.post_list, name='post_list'),
    url(r'^$', views.journeydefault, name='journeydefault'),
    url(r'^journeyadd', views.journeyadd, name='journeyadd'),

    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<post>[-\w]+)/$', views.post_detail, name='post_detail'),
    url(r'^(?P<post_id>\d+)/share/$', views.post_share, name='post_share'),

 #   url(r'^login/$', views.lo, name='login')

  #  url(r'^logout/$', views.logout, { 'template_name': 'registration/logged_out.html',}, name='logout' ),

    url(r'^account/', include('tjapp.templates.tjapp.account.urls'))

    # url(r'post/new/$', views.post_new, name='post_new')
]
