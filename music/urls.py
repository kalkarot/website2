
from django.conf.urls import url
from . import views

app_name = 'music'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    #/music/ album.id /
    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),

    url(r'^(?P<album_id>[0-9]+)/favorite/$', views.favorite, name='favorite'),
]
