from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^people/$', views.person_index, name='person_index'),
    url(r'^castles/$', views.castle_index, name='castle_index'),
    url(r'^regions/$', views.region_index, name='region_index'),
    url(r'^people/(?P<person_name>\w+_\w+)/$', views.person_detail, name='person_detail'),
    url(r'^regions/(?P<region_name>[a-zA-z ]+)/$', views.region_detail, name='region_detail'),
    url(r'^castles/(?P<castle_name>[\'a-zA-z ]+)/$', views.castle_detail, name='castle_detail'),
    url(r'^api/people/$', views.person_api_list),
    url(r'^api/castles/$', views.castle_api_list),
    url(r'^api/regions/$', views.region_api_list),
    url(r'^api/people/(?P<name>\w+_\w+)/$', views.person_api_detail),
    url(r'^api/regions/(?P<name>[a-zA-z ]+)/$', views.region_api_detail),
    url(r'^api/castles/(?P<name>[\'a-zA-z ]+)/$', views.castle_api_detail),
]
