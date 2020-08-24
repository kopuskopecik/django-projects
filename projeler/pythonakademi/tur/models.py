import datetime

from django.db import models
from django.urls import reverse
from django.utils.text import slugify

from ckeditor.fields import RichTextField

BAŞLIKLAR = (
	('python', 'Python'),
	('bootstrap4', 'Bootstrap4'),
	('html', 'HTML'),
	('css', 'CSS'),
	('javascript', 'Javascript'),
)

class Baslik(models.Model):
	baslik_adi = models.CharField("Üst Başlığın adı", max_length=100)
	ana_başlık = models.CharField(max_length=30, choices=BAŞLIKLAR, default = "python") 
	slug = models.SlugField(unique=True, max_length=130)
	modul_mu = models.BooleanField("Modül mü", default = False)
	icon_name = models.CharField("Icon ismi", max_length=50, blank = True)
	sıra = models.PositiveSmallIntegerField(blank= True)
	aktif = models.BooleanField("Aktif mi", default = False)
	

	
	def __str__(self):
		return self.baslik_adi
	
	def get_absolute_url(self):
		return reverse('tur:baslik-index', kwargs={'slug':self.slug},)
	
	def save(self, *args, **kwargs):
		self.slug = slugify(self.baslik_adi.replace("ı","i"))		
		return super(Baslik, self).save(*args, **kwargs)
	
	

# Create your models here.
class Dersler(models.Model):
	headline = models.CharField(max_length=100)
	content = RichTextField()
	slug = models.SlugField(unique=True, editable=False, max_length=130)
	number = models.PositiveSmallIntegerField()
	publishing_date = models.DateTimeField(verbose_name="yayımlanma_tarihi",auto_now_add=True)
	updating_date = models.DateTimeField(verbose_name="güncellenme_tarihi", blank = True, null = True)
	baslık = models.ForeignKey(Baslik, on_delete=models.CASCADE, verbose_name = "Üst Başlık")
	filtre1 = models.CharField(max_length=100, default = "-")
	filtre2 = models.CharField(max_length=100, default = "-")
	descriptions = models.CharField(max_length=500, default = "Python Dersleri")
	anahtar = models.CharField(max_length=500, default = "Python Dersleri")
	slug2 = models.SlugField( max_length=130, default = "python")
	views = models.PositiveSmallIntegerField(default = 0)
	aktif = models.BooleanField("Aktif mi", default = False)
	
	def __str__(self):
		return self.headline
	
	class Meta:
		ordering = ['number']
	
	def get_absolute_url(self):
		return reverse('tur:detail', kwargs={'slug':self.slug, 'slug2':self.baslık.slug})
		
	
	def get_create_url(self):
		return reverse('tur:create')
	
	def get_update_url(self):
		return reverse('tur:update', kwargs={'slug':self.slug, 'slug2':self.slug2})
	
	def get_delete_url(self):
		return reverse('tur:delete', kwargs={'slug':self.slug, 'slug2':self.slug2})
		
	def get_unique_slug(self):
		slug = slugify(self.headline.replace("ı","i"))
		unique_slug = slug
		counter = 1
		while Dersler.objects.filter(slug=unique_slug).exclude(publishing_date = self.publishing_date).exists():
			unique_slug = "{}-{}".format(slug, counter)
			counter +=1 
		return unique_slug
	
	def set_number(self):
		for i in Dersler.objects.filter(number__gte = self.number):
			i.number = i.number + 1
			i.save()
	
	def delete_number(self):
		for i in Dersler.objects.filter(number__gte = self.number):
			print(i)
			i.number = i.number - 1
			i.save()
		
	def save(self, *args, **kwargs):
		self.slug = self.get_unique_slug()
		if Dersler.objects.filter(publishing_date = self.publishing_date).exists():
			pass
		else:
			self.set_number()
		
		return super(Dersler, self).save(*args, **kwargs)
	
	def next_lesson(self):
		all_lessons = Dersler.objects.filter(aktif = True)
		all_lessons = list(all_lessons)
		ranking = all_lessons.index(self)
		if self == Dersler.objects.last():
			return all_lessons[0]
		
		else:
			return all_lessons[ranking + 1]

	def previous_lesson(self):
		all_lessons = Dersler.objects.filter(aktif = True)
		all_lessons = list(all_lessons)
		ranking = all_lessons.index(self)
		if self == Dersler.objects.first():
			return all_lessons[-1]
		
		else:
			return all_lessons[ranking - 1]
	
	def clean(self):
		self.updating_date = datetime.datetime.now()