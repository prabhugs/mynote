__author__ = 'prabhugs'

from django.conf.urls import patterns, url

from notes import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^(?P<post_id>\d+)/$', views.detail, name='detail'),
                       url(r'^(?P<post_id>\d+)/comments/$', views.comments, name='comments'),
                       )