from django.urls import path

from .views import (baslik_listesi, BaslikOlusturView, ders_degistir, baslik_detail, BaslikUpdateView, 
					ders_ekle, BaslikDeleteView, ders_guncelle, ders_sil, soru_ekle,
					soru_sil, sorulara_cevap_ekle, take_quiz, take_baslik_quiz, alistirma_yap,
					alistirma_sonucu_hesapla)

app_name = "dersler"
urlpatterns = [
    path('', baslik_listesi, name = "baslik_listesi"),
	path('baslik-ekle/', BaslikOlusturView.as_view(), name = "baslik_olustur"),
	path('baslik/<int:pk>/', baslik_detail, name='baslik_detail'),
	path('baslik/<int:baslik_pk>/ders/<int:ders_pk>/', ders_degistir, name='ders_degistir'),
	path('baslik/<int:pk>/guncelle/', BaslikUpdateView.as_view(), name='baslik_guncelle'),
    path('baslik/<int:pk>/delete/', BaslikDeleteView.as_view(), name='baslik_sil'),
    #path('quiz/<int:pk>/results/', teachers.QuizResultsView.as_view(), name='quiz_results'),
    path('baslik/<int:baslik_pk>/ders/ekle/', ders_ekle, name='ders_ekle'),
	path('baslik/<int:baslik_pk>/ders/<int:ders_pk>/guncelle/', ders_guncelle, name='ders_guncelle'),
	path('baslik/<int:pk>/ders/sil/', ders_sil, name='ders_sil'),
	path('baslik/<int:baslik_pk>/ders/<int:ders_pk>/soru-ekle/', soru_ekle, name='soru_ekle'),
	path('baslik/ders/<int:pk>/soru/sil/', soru_sil, name='soru_sil'),
	path('baslik/<int:baslik_pk>/ders/<int:ders_pk>/soru/<int:soru_pk>/', sorulara_cevap_ekle, name='sorulara_cevap_ekle'),
	path('quiz/<int:pk>/', take_quiz, name='take_quiz'),
	path('quiz/baslik/<int:pk>/', take_baslik_quiz, name='take_baslik_quiz'),
	path('baslik/<int:pk>/alistirma/', alistirma_yap, name='alistirma_yap'),
	path('baslik/<int:pk>/alistirma-sonucu-hesapla/', alistirma_sonucu_hesapla, name='alistirma_sonucu_hesapla'),
	#path('quiz/baslik/<int:pk>/dogru', dogru_cevap_, name='alistirma_sonucu_hesapla'),
    #path('quiz/<int:quiz_pk>/question/<int:question_pk>/', teachers.question_change, name='question_change'),
    #path('quiz/<int:quiz_pk>/question/<int:question_pk>/delete/', teachers.QuestionDeleteView.as_view(), name='question_delete'),
	
]