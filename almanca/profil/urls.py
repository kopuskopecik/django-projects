from django.urls import path

from .views import (ogrenci_profil, ogretmen_profil,favorilere_baslik_ekle, 
					favoriler, derslerim, sorular, ders_olustur, begen)

app_name = "profil"
urlpatterns = [
	path('ogretmen/<int:ogretmen_id>/', ogretmen_profil, name='ogretmen_profil'),
	path('ogrenci/<int:ogrenci_id>/', ogrenci_profil, name='ogrenci_profil'),
	path('ogrenci/<int:baslik_id>/ekle/', favorilere_baslik_ekle, name='favorilere_baslik_ekle'),
	path('ogrenci/<int:baslik_id>/begen/', begen, name='begen'),
	path('ogrenci/<int:ogrenci_id>/favoriler/', favoriler, name='favoriler'),
	path('ogrenci/<int:ogrenci_id>/dersler/', derslerim, name='derslerim'),
	path('ogrenci/<int:ogrenci_id>/sorular/', sorular, name='sorular'),
	path('ogrenci/<int:ogrenci_id>/ders-olustur/', ders_olustur, name='ders_olustur'),
]