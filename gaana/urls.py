from django.conf.urls import patterns, url
from gaana import views

urlpatterns = patterns('',
                url(r'^$', views.index, name='index'),
                url(r'^artist/(?P<artist_name_slug>[\w\-]+)/$', views.artist, name='artist'),
                url(r'^register/$', views.register, name='register'),
                url(r'^login/$', views.user_login, name='login'),
                url(r'^logout/$', views.user_logout, name='logout'),
                )