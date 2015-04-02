from django.conf.urls import patterns, include, url
from django.contrib import admin
from home import views
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bookSwap.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'home/', include('home.urls')),
    url(r'^$', views.index, name='index'),
)
