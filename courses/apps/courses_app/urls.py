from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^process$', views.process),
    url(r'^courses/destroy/(?P<number>\d+)$', views.destroy),
    url(r'^courses/remove/(?P<number>\d+)$', views.remove),
]