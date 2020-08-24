import uuid

from django.db import models
from django.utils.text import slugify
from django.shortcuts import reverse
from django.contrib.auth.models import User
from django.utils.html import escape
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from django.conf import settings
from django.contrib.auth import get_user_model


STATUS_CHOICES1 = (
    ('d', 'Draft'),
    ('p', 'Published'),
    ('w', 'Withdrawn'),
)

STATUS_CHOICES = (
    ('t', 'Turuncu'),
    ('m', 'Mavi'),
    ('k', 'Kırmızı'),
	('s', 'Sarı'),
	('y', 'Yeşil'),
)

ETKINLIK_CHOICES = (
	('k', 'Kitap Okuma Turnuvası'),
    ('p', 'Kitap Okuma Etkinlikleri'),
    ('a', 'Anlamayı Geliştirme Turnuvası'),
    ('b', 'Birinci Sınıf Okuma Etkinliği'),
	('o', 'Okul Öncesi Masal Etkinliği'),
	('l', 'Lise "Kitap Koçum" Etkinliği'),
)

ODUL_CHOICES = (
	('b', 'Birinci Ödül'),
    ('i', 'İkinci Ödül'),
    ('ü', 'Üçüncü Ödül'),
    ('d', 'Dördüncü Ödül'),
)

def get_sentinel_user():
	return get_user_model().objects.get_or_create(username='deleted')[0]
	
class Model1(models.Model):
	number = models.PositiveSmallIntegerField(default = 0)
	
	class Meta:
		ordering = ["number",]
		default_permissions = ()
	
	def __str__(self):
		return str(self.number)

		
class Model2(models.Model):
	number = models.PositiveSmallIntegerField(default = 0)
	isim = models.CharField(max_length=50)
	
	class Meta:
		ordering = ["number",]
		#default_permissions = ()
		indexes = [
			models.Index(fields=['number', 'isim']),
			models.Index(fields=['isim'], name='isim_idx'),
		]
		
		#unique_together = [['number', 'isim']]
		unique_together = ['number', 'isim']
		#constraints = [
		#	models.CheckConstraint(check=models.Q(number__gte=18), name='number_gte_18'),
		#]
		
	
	def __str__(self):
		return self.isim
		
	def clean(self):
		if self.number > 100:
			raise ValidationError({'number': _("Number 100'den büyük olmamalı")})


			
			
class Place(models.Model):
	name = models.CharField(max_length=50)
	address = models.CharField(max_length=80, blank = True)
	def __str__(self):
		return self.name

class Restaurant(Place):
	serves_hot_dogs = models.BooleanField(default=False)
	serves_pizza = models.BooleanField(default=False)			

class Base(models.Model):
	m2m = models.ManyToManyField(
		'Article',
		related_name="%(app_label)s_%(class)s_related",
		related_query_name="%(app_label)s_%(class)ss",
	)
	class Meta:
		abstract = True

class ChildA(Base):
	pass

class ChildB(Base):
	pass

class Article(models.Model):
	name = models.CharField(max_length=50, unique=True, db_index = True)
	slug = models.SlugField(unique=True, max_length=130)
	publishing_date = models.DateTimeField(auto_now_add=True)
	#publishing_date = models.DateTimeField()
	updating_date = models.DateTimeField(auto_now=True)
	status = models.CharField(max_length=1, choices=STATUS_CHOICES1)
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='kullanicilar', default = 1, help_text = escape("<b>akıllı olun</b>"), db_index = False)
	
	
	def __str__(self):
		return self.name
	
	def get_absolute_url(self):
		return reverse('denemeler:article-detail', kwargs={'slug':self.slug})
		
	
	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		return super(Article, self).save(*args, **kwargs)
	
	def my_property(self):
		return self.name + ' ' + self.status
	my_property.short_description = "Full name of the person"
	full_name = property(my_property)

class Teacher(models.Model):
	isim = models.CharField(max_length= 100, blank = True)
	
	def __str__(self):
		return self.isim
		

class Kitap(models.Model):
	isim = models.CharField(max_length= 30, blank = True)
	sayfa = models.PositiveIntegerField()

	def __str__(self):
		return self.isim
	
	
class Student(models.Model):
	isim = models.CharField(max_length= 30, blank = True)
	teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='teachers')
	kitap = models.ManyToManyField(Kitap, related_name='kitaplar', blank = True)
	takim = models.CharField(max_length=1, choices=STATUS_CHOICES, blank = True)
	bireysel_odulu = models.CharField(max_length= 30, blank = True)
	takim_odulu	= models.CharField(max_length= 30, blank = True)
	
	def __str__(self):
		return self.isim
	
	 
class Sinif(models.Model):
	isim = models.CharField(max_length= 30)
	asistan = models.ManyToManyField(Student, related_name='asistanlar', blank = True)
	ogrenci = models.ManyToManyField(Student, related_name='ogrenciler', blank = True)
	#hedef = models.PositiveIntegerField(blank = True, null = True)
	ogretmen = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='ogretmenler', blank = True, null = True)
	#okunan = models.PositiveIntegerField(blank = True)
	
	def __str__(self):
		return self.isim
	

class Etkinlik(models.Model):
	isim = models.CharField(max_length=1, choices=ETKINLIK_CHOICES, blank = True)
	sinif =models.ForeignKey(Sinif, on_delete=models.CASCADE, related_name='siniflar', blank = True, null = True)
	hedef = models.PositiveIntegerField(blank = True)
	ogretmen = models.ForeignKey(Teacher, on_delete=models.CASCADE, blank = True, null = True)
	startting_date = models.DateTimeField(max_length= 30, auto_now_add=True)
	finishing_date = models.DateTimeField(max_length= 30, auto_now=True)
	odul = models.CharField(max_length=1, choices=ODUL_CHOICES, blank = True)

	def __str__(self):
		return self.isim


class Blog(models.Model):
	name = models.CharField(max_length=100)
	tagline = models.TextField()
	
	def __str__(self):
		return self.name

class Author(models.Model):
	name = models.CharField(max_length=200)
	email = models.EmailField()
	age = models.IntegerField()
	
	def __str__(self):
		return self.name

class Entry(models.Model):
	blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
	headline = models.CharField(max_length=255)
	body_text = models.TextField()
	pub_date = models.DateField()
	mod_date = models.DateField()
	authors = models.ManyToManyField(Author)
	n_comments = models.IntegerField()
	n_pingbacks = models.IntegerField()
	rating = models.IntegerField()
	
	def __str__(self):
		return self.headline


		
class Publisher(models.Model):
	name = models.CharField(max_length=300)
	
	def __str__(self):
		return self.name

class Book(models.Model):
	name = models.CharField(max_length=300)
	pages = models.IntegerField()
	price = models.DecimalField(max_digits=10, decimal_places=2)
	rating = models.FloatField()
	authors = models.ManyToManyField(Author)
	publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
	pubdate = models.DateField()

	def __str__(self):
		return self.name

class Store(models.Model):
	name = models.CharField(max_length=300)
	books = models.ManyToManyField(Book)
	
	def __str__(self):
		return self.name
		
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class TaggedItem(models.Model):
	tag = models.SlugField()
	content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.tag
