import datetime

from django.db import models
from django.urls import reverse
from django.utils.text import slugify

from ckeditor.fields import RichTextField

from tur.models import Dersler

BAŞLIKLAR = (
	('python', 'Python'),
	('bootstrap4', 'Bootstrap4'),
	('html', 'HTML'),
	('css', 'CSS'),
)

class Topic(models.Model):
	baslik_adi = models.CharField("Üst Başlığın adı", max_length=100)
	ana_başlık = models.CharField(max_length=30, choices=BAŞLIKLAR, default = "python") 
	slug = models.SlugField(unique=True,max_length=130)
	modul_mu = models.BooleanField("Modül mü", default = False)
	icon_name = models.CharField("Icon ismi", max_length=50, blank = True)
	sıra = models.PositiveSmallIntegerField(blank= True, default = 0)
	aktif = models.BooleanField("Aktif mi", default = False)
	
	def __str__(self):
		return self.baslik_adi
	
	def get_absolute_url(self):
		return reverse('ingilizce:baslik-index', kwargs={'slug':self.slug},)
	
	def save(self, *args, **kwargs):
		self.slug = slugify(self.baslik_adi.replace("ı","i"))		
		return super(Topic, self).save(*args, **kwargs)	

		
#class Yorum(models.Model):
	
#	pass
		

class Lesson(models.Model):
	headline = models.CharField(max_length=100)
	content = RichTextField()
	slug = models.SlugField(unique=True, editable=False, max_length=130)
	number = models.PositiveSmallIntegerField()
	publishing_date = models.DateTimeField(verbose_name="yayımlanma_tarihi",auto_now_add=True)
	updating_date = models.DateTimeField(verbose_name="güncelleme_tarihi", null=True, blank = True)
	baslık = models.ForeignKey(Topic, on_delete=models.CASCADE, verbose_name = "Üst Başlık")
	filtre1 = models.CharField(max_length=100, default = "-")
	filtre2 = models.CharField(max_length=100, default = "-")
	descriptions = models.CharField(max_length=500, default = "Python Dersleri")
	anahtar = models.CharField(max_length=500, default = "Python Dersleri")
	slug2 = models.SlugField( max_length=130, default = "python")
	views = models.PositiveSmallIntegerField(default = 0)
	aktif = models.BooleanField("Aktif mi", default = False)
	#yorum = models.ForeignKey(Yorum, on_delete=models.CASCADE, verbose_name = "Yorum")
	
	def __str__(self):
		return self.headline
	
	class Meta:
		ordering = ['number']
	
	def get_absolute_url(self):
		return reverse('ingilizce:detail', kwargs={'slug':self.slug, 'slug2':self.baslık.slug})

	def hreflang_get_absolute_url(self):
		#if self.number < 486:
		if Dersler.objects.filter(number = self.number).exists():
			lesson = Dersler.objects.get(number = self.number)
			return reverse('tur:detail', kwargs={'slug':lesson.slug, 'slug2':lesson.slug2})
		return reverse('home')
	def get_create_url(self):
		return reverse('ingilizce:create')
	
	def get_update_url(self):
		return reverse('ingilizce:update', kwargs={'slug':self.slug, 'slug2':self.slug2})
	
	def get_delete_url(self):
		return reverse('ingilizce:delete', kwargs={'slug':self.slug, 'slug2':self.slug2})	
		
	def set_number(self):
		for i in Lesson.objects.filter(number__gte = self.number):
			i.number = i.number + 1
			i.save()
	
	def get_unique_slug(self):
		slug = slugify(self.headline.replace("ı","i"))
		unique_slug = slug
		slug2 = slugify(self.filtre1.replace("ı","i"))
		self.slug2 = slug2
		counter = 1
		while Lesson.objects.filter(slug=unique_slug).exclude(publishing_date = self.publishing_date).exists():
			unique_slug = "{}-{}".format(slug, counter)
			counter +=1 
		return unique_slug
	
	def save(self, *args, **kwargs):
		self.slug = self.get_unique_slug()
		if Lesson.objects.filter(publishing_date = self.publishing_date).exists():
			pass
		else:
			self.set_number()
		
		return super(Lesson, self).save(*args, **kwargs)
		
	def all_lessons(self):
		return Lesson.objects.all()
	
	def next_lesson(self):
		all_lessons = Lesson.objects.filter(aktif = True)
		all_lessons = list(all_lessons)
		ranking = all_lessons.index(self)
		if self == Lesson.objects.last():
			return all_lessons[0]
		
		else:
			return all_lessons[ranking + 1]

	def previous_lesson(self):
		all_lessons = Lesson.objects.filter(aktif = True)
		all_lessons = list(all_lessons)
		ranking = all_lessons.index(self)
		if self == Lesson.objects.first():
			return all_lessons[-1]
		
		else:
			return all_lessons[ranking - 1]
	
	def set_number(self):
		for i in Lesson.objects.filter(number__gte = self.number):
			i.number = i.number + 1
			i.save()
	
	def delete_number(self):
		for i in Lesson.objects.filter(number__gte = self.number):
			print(i)
			i.number = i.number - 1
			i.save()
			
	def clean(self):
		self.updating_date = datetime.datetime.now()
		