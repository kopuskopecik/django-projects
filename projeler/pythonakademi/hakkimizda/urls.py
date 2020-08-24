from django.urls import path
from django.conf.urls import url
from .views import *

app_name="hakkimizda"

urlpatterns = [

	path('hakkimizda/', hakkimizda, name="hak"),
]