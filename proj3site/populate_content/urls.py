from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<person_name>\w+_\w+)/$', views.person_detail, name='person_detail'),
    url(r'^people/$', views.person_api_list),
    url(r'^people/(?P<pk>[0-9]+)/$', views.person_api_detail_pk),
    url(r'^people/(?P<person_name>\w+_\w+)/$', views.person_api_detail_name),
]

