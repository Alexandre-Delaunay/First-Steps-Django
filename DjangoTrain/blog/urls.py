from . import views
from django.urls import include, re_path

urlpatterns = [
    re_path(r'^$', views.index),
    re_path(r'^articles/(?P<id>[0-9]+)$', views.show),
]
