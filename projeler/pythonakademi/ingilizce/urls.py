from django.urls import path
from . import views

app_name = 'ingilizce'
urlpatterns = [
    path('', views.home_view, name='ing-home'),
	path('python-lessons/', views.ing_index, name="index"),
	path('create/', views.ing_create, name='create'),
	path('ara', views.ing_ara, name="ara"),
	#path('django-lessons/', views.django_index, name="django-index"),
	path('tkinter-lessons/', views.tkinter_index, name="tkinter-index"),
	path('modules-and-packages/', views.modul_index, name="modul-index"),
	path('<slug:slug>/', views.baslik_index, name="baslik-index"),
	path('<slug:slug2>/<slug:slug>/update/', views.ing_update, name='update'),
	path('<slug:slug2>/<slug:slug>/', views.ing_detail, name="detail"),
    #path('<slug:slug2>/<slug:slug>/', views.LessonDetailView.as_view(), name='detail'),
	path('<slug:slug2>/<slug:slug>/delete/', views.ing_delete, name="delete"),
]