from django.urls import include, path

from .views import pdf_view, pdf_create, print_users


app_name = "belgeler"
urlpatterns = [
    path('pdf/', pdf_view, name='pdf_goster'),
	path('<int:pk>pdf/create/', pdf_create, name='pdf_create'),
	path('<int:pk>/print-users/', print_users, name='print_users'),
    
]