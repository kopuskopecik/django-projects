from django.urls import path
from django.conf.urls import url
from .views import *

app_name="front"

urlpatterns = [
	#path('front/', home_view, name="front-home"),
	path('javascript-dersleri/', front_index, name="index"),
	path('front/create/', front_create, name="create"),
	path('front/ara', front_ara, name="ara"),
	path('front/<slug:slug>/', baslik_index, name="baslik-index"),
	path('front/<slug:slug2>/<slug:slug>/', front_detail, name="detail"),
	path('front/<slug:slug2>/<slug:slug>/update/', front_update, name="update"),
	path('front/<slug:slug2>/<slug:slug>/delete/', front_delete, name="delete"),
]