from django.urls import path

from .views import ogretmen, etkinlik_olustur, etkinliklerim, etkinlik_detail, ogrenciler

app_name = "turnuva"
urlpatterns = [
	path('<int:teacher_id>/', ogretmen, name='ogretmen'),
	path('<int:teacher_id>/etkinlik/', etkinlik_olustur, name='etkinlik_olustur'),
	path('<int:teacher_id>/etkinliklerim/', etkinliklerim, name='etkinliklerim'),
	path('<int:teacher_id>/etkinliklerim/<int:etkinlik_id>/', etkinlik_detail, name='etkinlik-detail'),
	path('<int:teacher_id>/etkinliklerim/<int:etkinlik_id>/ogrenciler/', ogrenciler, name='ogrenciler'),
	
]