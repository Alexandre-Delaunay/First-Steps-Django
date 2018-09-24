from django.contrib import admin
from django.urls import include, re_path
from django.conf.urls import handler404, handler500
from . import views

handler404 = 'DjangoTrain.views.handler404'
handler500 = 'DjangoTrain.views.handler500'

app_name='DjangoTrain'

urlpatterns = [
    re_path(r'^$', views.home, name='home'),
    re_path(r'^about/$', views.about, name='about'),
    re_path(r'^contact/$', views.contact, name='contact'),
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^blog/', include('blog.urls'))
]
