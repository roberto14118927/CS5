from django.urls import path, re_path
from django.conf.urls import include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

from ejemplo import views



urlpatterns =  [
    re_path(r'^ejemplo/$', views.ProfileList.as_view())
]