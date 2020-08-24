from django.urls import path
from .views import home, park, unpark, parking_info

app_name = "cars"
urlpatterns = [
    path('', home, name = "home"),
    path('car/<int:pk>/', park, name='park'),
    path('slot/<int:pk>/', unpark, name='unpark'),
    path('get/<int:pk>/', parking_info, name='parking_info'),
    
]