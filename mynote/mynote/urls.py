from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mynote.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^$', include('notes.urls')),
    url(r'^notes/', include('notes.urls', namespace="notes")),
    url(r'^admin/', include(admin.site.urls)),

)
