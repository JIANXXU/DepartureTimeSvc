from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from services import views

urlpatterns = patterns('services.views',
    url(r'^departuretime/$', views.DepartureTimeList.as_view()),
)

urlpatterns = format_suffix_patterns(urlpatterns)