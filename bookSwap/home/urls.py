from django.conf.urls import patterns, url
from django.contrib.auth import urls
from home import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
    url(r'^login/$', views.user_login, name='login'),
	url(r'^register/$', views.register, name='register'),
	url(r'^about/$', views.about, name='about'),
	url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^filebook/$', views.file_book, name='file_book'),
    url(r'^viewbooks/$', views.view_books, name='view_books'),
    url(r'^viewallbooks/$', views.viewallbooks, name='viewallbooks'),
    url(r'^viewbooks/(?P<book_name_url>\w+)/$', views.view_book, name='book_name_url'),
    url(r'^editbook/(?P<book_pk>\w+)/$', views.edit_book, name='book_name_url'),
	url(r'^search/$', views.search, name='search'),
    url(r'^accountinfo/$', views.accountinfo, name='accountinfo'), 
    url(r'^homepage/$', views.homepage, name='homepage'),
    url(r'^deletebook/(?P<book_id>\w+)/$', views.delete_book, name='book_name_url'),
	)