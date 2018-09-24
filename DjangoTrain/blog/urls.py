from . import views
from django.urls import include, re_path

app_name='blog'

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^articles/(?P<id>[0-9]+)$', views.show, name='show'),
]
