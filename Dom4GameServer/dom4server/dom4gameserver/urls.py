from django.conf.urls import patterns, url

from dom4gameserver import views


urlpatterns = patterns('',
            url(r'^$', views.index, name='index'),
            url(r'^newgame', views.newgame, name='newgame'),
            url(r'^newrequest$', views.newrequest, name='newrequest'),
            url(r'^game/(?P<gameid>\d+)$', views.viewgame, name='viewgame'),
            url(r'^(?P<req_id>\d+)/approve$', views.approve, name='approverequest'),
            url(r'^(?P<req_id>\d+)/close$', views.close, name='closerequest')
            )
