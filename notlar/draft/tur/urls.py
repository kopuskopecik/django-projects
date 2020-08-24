from django.urls import path
from django.conf.urls import url
from .views import *

app_name="tur"

urlpatterns = [

	path('python-dersleri/', tur_index, name="index"),
	url('create/', tur_create, name="create"),
	url(r'^(?P<slug2>[\w-]+)/$', ana_index, name="ana_index"),
	url(r'^(?P<slug2>[\w-]+)/(?P<slug>[\w-]+)/$', tur_detail, name="detail"),
	url(r'^(?P<slug2>[\w-]+)/(?P<slug>[\w-]+)/update/', tur_update, name="update"),
	url(r'^(?P<slug2>[\w-]+)/(?P<slug>[\w-]+)/delete/', tur_delete, name="delete"),
]