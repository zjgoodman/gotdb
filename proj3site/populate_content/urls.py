from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^people/$', views.person_index, name='person_index'),
    url(r'^castles/$', views.castle_index, name='castle_index'),
    url(r'^regions/$', views.region_index, name='region_index'),
    url(r'^people/(?P<person_name>\w+_\w+)/$', views.person_detail, name='person_detail'),
    url(r'^regions/(?P<region_name>[a-zA-z ]+)/$', views.region_detail, name='region_detail'),
    url(r'^castles/(?P<castle_name>\w+)/$', views.castle_detail, name='castle_detail'),
]

