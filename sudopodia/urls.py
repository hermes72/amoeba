from django.conf.urls import include, url
from django.contrib import admin
from . import views
urlpatterns = [
    url(r'^api$', views.api),
    url(r'^api/$', views.api),
    url(r'^requestapi/$', views.requestapi),
    url(r'^requestapi$', views.requestapi),
    url(r'^$', views.index)
]
