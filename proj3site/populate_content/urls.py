from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^test/$', views.test),
    url(r'^(?P<person_name>\w+_\w+)/$', views.person_detail, name='person_detail'),
]

