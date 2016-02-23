from django.conf.urls import include, url
from django.contrib import admin
from . import views
urlpatterns = [
    url(r'^api$', views.api),
    url(r'^api/(?P<eventid>[0-9]+)/$', views.apifrom),
    url(r'^requestapi/$', views.requestapi),
    url(r'^requestapi$', views.requestapi),
    url(r'^postpage$',views.postpage),
    url(r'^postevent$',views.eventsubmit),
    url(r'^$', views.index)
]
