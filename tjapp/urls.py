from django.conf.urls import url, include
from . import views

urlpatterns = [
    # url(r'^$', views.post_list, name='post_list'),
    url(r'^$', views.journey_default, name='journey_default'),
    url(r'^journey_add', views.journey_add, name='journey_add'),

    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<post>[-\w]+)/$', views.post_detail, name='post_detail'),
    url(r'^(?P<post_id>\d+)/share/$', views.post_share, name='post_share'),

   # url(r'post/new/$', views.post_new, name='post_new')
]
