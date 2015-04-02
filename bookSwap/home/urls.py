from django.conf.urls import patterns, url
from django.contrib.auth import urls
from home import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^login/$', views.login, name='login'),
	)