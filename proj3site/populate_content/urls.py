from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/', views.about_index, name='about_index'),

    url(r'^people/$', views.person_index, name='person_index'),
    url(r'^castles/$', views.castle_index, name='castle_index'),
    url(r'^regions/$', views.region_index, name='region_index'),
    url(r'^houses/$', views.house_index, name='house_index'),

    url(r'^people/(?P<person_id>[a-z_]+)/$', views.person_detail, name='person_detail'),
    url(r'^regions/(?P<region_id>[a-z_]+)/$', views.region_detail, name='region_detail'),
    url(r'^castles/(?P<castle_id>[a-z_]+)/$', views.castle_detail, name='castle_detail'),
    url(r'^houses/(?P<house_id>[a-z_]+)/$', views.house_detail, name='house_detail'),

    url(r'^api/people/$', views.person_api_list),
    url(r'^api/castles/$', views.castle_api_list),
    url(r'^api/regions/$', views.region_api_list),
    url(r'^api/houses/$', views.house_api_list),
    url(r'^api/authors/$', views.author_api_list),

    url(r'^api/people/(?P<person_id>[a-z_]+)/$', views.person_api_detail),
    url(r'^api/regions/(?P<region_id>[a-z_]+)/$', views.region_api_detail),
    url(r'^api/castles/(?P<castle_id>[a-z_]+)/$', views.castle_api_detail),
    url(r'^api/houses/(?P<house_id>[a-z_]+)/$', views.house_api_detail),
    url(r'^api/authors/(?P<author_id>[a-z_]+)/$', views.author_api_detail),

    url(r'^all_castles/$', views.all_castles_index, name='all_castles_index'),
    url(r'^all_regions/$', views.all_regions_index, name='all_regions_index'),
    url(r'^all_people/$', views.all_people_index, name='all_people_index'),
    url(r'^all_houses/$', views.all_houses_index, name='all_houses_index'),
]
