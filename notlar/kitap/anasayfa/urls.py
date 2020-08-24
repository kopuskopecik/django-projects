from django.urls import path

from . import views

app_name = 'anasayfa'
urlpatterns = [
    path('', views.AnaSayfa.as_view(), name='anasayfa'),
    path('genel/<slug:slug>/', views.GenelDetailView.as_view(), name='genel-detail'),
    #path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    #path('<int:question_id>/vote/', views.vote, name='vote'),
]