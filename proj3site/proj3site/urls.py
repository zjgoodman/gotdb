from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'proj3site.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^', include('splash.urls')),
    url(r'^people/', include('populate_content.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
