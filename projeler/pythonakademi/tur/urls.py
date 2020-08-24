from django.urls import path
from django.conf.urls import url
from .views import *

app_name="tur"

urlpatterns = [

	path('python-dersleri/', tur_index, name="index"),
	path('django-dersleri/', django_index, name="django-index"),
	path('tkinter-dersleri/', tkinter_index, name="tkinter-index"),
	path('modul-ve-paketler/', modul_index, name="modul-index"),
	path('create/', tur_create, name="create"),
	path('ara', tur_ara, name="ara"),
	path('<slug:slug>/', baslik_index, name="baslik-index"),
	path('<slug:slug2>/<slug:slug>/', tur_detail, name="detail"),
	url(r'^(?P<slug2>[\w-]+)/(?P<slug>[\w-]+)/update/', tur_update, name="update"),
	url(r'^(?P<slug2>[\w-]+)/(?P<slug>[\w-]+)/delete/', tur_delete, name="delete"),
]