from django.conf.urls import include, url
from django.contrib import admin
from . import views
urlpatterns = [
    url(r'^api$', views.api),
    url(r'^api/$', views.api),
    url(r'^register/$', views.registerevent),
    url(r'^register$', views.registerevent),
    url(r'^$', views.index)
]
