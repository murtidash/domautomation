from django.conf.urls import patterns, include, url

from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dom4server.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^dom4/', include('dom4gameserver.urls', namespace='dom4gameserver')),
    url(r'^admin/', include(admin.site.urls)),

)


urlpatterns += staticfiles_urlpatterns()