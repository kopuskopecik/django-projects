from django.urls import path
from . import views

app_name = 'ingilizce'
urlpatterns = [
    path('', views.LessonIndexView.as_view(), name='index'),
	path('python-lessons/', views.LessonAllIndexView.as_view(), name="all_index"),
	path('create/', views.LessonCreateView.as_view(), name='create'),
	path('about/', views.LessonTemplateView.as_view(), name='about'),
	path('<slug:slug2>/', views.AnaIndexView.as_view(), name='ana_index'),
	path('<slug:slug2>/<slug:slug>/update/', views.LessonUpdateView.as_view(), name='update'),
    path('<slug:slug2>/<slug:slug>/', views.LessonDetailView.as_view(), name='detail'),
	path('<slug:slug2>/<slug:slug>/delete/', views.ing_delete, name="delete"),
]