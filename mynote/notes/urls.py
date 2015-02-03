__author__ = 'prabhugs'

from django.conf.urls import patterns, url

from notes import views

urlpatterns = patterns('',
                       url(r'^$', views.IndexView.as_view(), name='index'),
                       url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
                       url(r'^(?P<pk>\d+)/comments/$', views.CommentsView.as_view(), name='comments'),
                       url(r'^(?P<pk>\d+)/results/$', views.ResultsView.as_view(), name='results'),
                       url(r'^(?P<post_id>\d+)/comment/$', views.comment, name='comment'),
                       )