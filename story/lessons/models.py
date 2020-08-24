from django.db import models
from accounts.models import User
from django.shortcuts import render, reverse

from ckeditor.fields import RichTextField


# Create your models here.

class Baslik(models.Model):
	title = models.CharField(max_length = 100)
	owner = models.ForeignKey(User, on_delete=models.CASCADE)
	content = models.TextField(blank = True)
	ranking = models.IntegerField("Sıra", default = 0)
	publishing_date = models.DateTimeField(verbose_name="yayımlanma_tarihi",auto_now_add=True)
	updating_date = models.DateTimeField(verbose_name="güncellenme_tarihi", auto_now = True)
	#dosya_yolu = models.FilePathField(path="elma/")
	youtube_urli = models.URLField("Youtube Url Adresi", blank = True)
	views = models.IntegerField(default = 0)
	favori_sayisi = models.IntegerField(default = 0)
	begenilme_sayisi = models.IntegerField(default = 0)
	
	# managers
	objects = models.Manager()
	
	def __str__(self):
		return self.title
	
	def degistir(self):
		return reverse('lessons:baslik_guncelle', kwargs={'pk':self.pk})
		
	def get_absolute_url(self):
		return reverse('lessons:baslik_detail', kwargs={'pk':self.pk})
		
	def ders_sayisi(self):
		#return Ders.objects.filter(baslik = self).count()
		return self.ders_set.count()
		
	def ders_var_mi(self):
		if self.ders_set.exists():
			return True
		return False

class Ders(models.Model):
	baslik = models.ForeignKey(Baslik, on_delete=models.CASCADE)
	title = models.CharField("Dersinizin Başlığı:",max_length = 100)
	content = RichTextField("İçerik:", blank = True)
	ranking = models.IntegerField("Sıra:", default = 0)
	example = models.CharField(max_length = 100, blank = True)
	publishing_date = models.DateTimeField(verbose_name="yayımlanma_tarihi",auto_now_add=True)
	updating_date = models.DateTimeField(verbose_name="güncellenme_tarihi", auto_now = True)
	youtube_urli = models.URLField("Youtube linki:", blank = True)
		
	
	def __str__(self):
		return self.title
	
	def guncelle(self):
		return reverse('lessons:ders_guncelle', kwargs={'baslik_pk':self.baslik.pk, 'ders_pk':self.pk})
	
	def sil(self):
		return reverse('lessons:ders_sil', kwargs={'pk':self.pk})
		
	def get_absolute_url(self):
		return reverse('lessons:ders_guncelle', kwargs={'baslik_pk':self.baslik.pk, 'ders_pk':self.pk})

	def soru_var_mi(self):
		if self.question_set.exists():
			return True
		return False
		
	def soru_sayisi(self):
		return self.question_set.all().count()
		
class Question(models.Model):
	ders = models.ForeignKey(Ders, on_delete=models.CASCADE)
	content = models.TextField(blank = True)
	ranking = models.IntegerField("Sıra:", default = 0)

	def __str__(self):
		return self.content
	
	def sil(self):
		return reverse('lessons:soru_sil', kwargs={'pk':self.pk})
	
	def cevap_sayisi(self):
		return self.answer_set.all().count()
	
	def get_absolute_url(self):
		return reverse('lessons:sorulara_cevap_ekle', kwargs={'baslik_pk':self.ders.baslik.pk, 'ders_pk':self.ders.pk, 'soru_pk':self.pk})

	def dogru_cevabi_getir(self):
		return self.answer_set.all().get(dogru_cevap = True)
		
class Answer(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	content = models.CharField("cevap", max_length = 100)
	dogru_cevap = models.BooleanField(default=False)
	
	def __str__(self):
		return self.content
		
class TakenQuiz(models.Model):
	student = models.ForeignKey('accounts.Student', on_delete=models.CASCADE)
	quiz = models.ForeignKey(Ders, on_delete=models.CASCADE)
	score = models.FloatField()
	date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.quiz.title

class TakenBaslikQuiz(models.Model):
	student = models.ForeignKey('accounts.Student', on_delete=models.CASCADE)
	baslik = models.ForeignKey(Baslik, on_delete=models.CASCADE)
	score = models.FloatField()
	date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.baslik.title


class StudentAnswer(models.Model):
	student = models.ForeignKey('accounts.Student', on_delete=models.CASCADE)
	answer = models.ForeignKey(Answer, on_delete=models.CASCADE)

	def __str__(self):
		return self.answer.content

class StudentBaslikAnswer(models.Model):
	student = models.ForeignKey('accounts.Student', on_delete=models.CASCADE)
	answer = models.ForeignKey(Answer, on_delete=models.CASCADE)

	def __str__(self):
		return self.answer.content
	

