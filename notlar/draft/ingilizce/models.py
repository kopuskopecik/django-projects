from django.db import models
from django.urls import reverse
from django.utils.text import slugify

from ckeditor.fields import RichTextField

from tur.models import Dersler

class MyManager(models.Manager):
	use_for_related_fields = True
	
	def general1(self, **kwargs):
		return self.filter(filtre2 = "ana1")
	
	def general2(self, **kwargs):
		return self.filter(filtre2 = "ana2")
	
	def modules(self, **kwargs):
		return self.filter(filtre2 = "ana3")
	
	def packet1(self, **kwargs):
		return self.filter(filtre2 = "ana4")
	
	def packet2(self, **kwargs):
		return self.filter(filtre2 = "ana5")
	

		

class Lesson(models.Model):
	headline = models.CharField(max_length=100)
	content = RichTextField()
	slug = models.SlugField(unique=True, editable=False, max_length=130)
	number = models.PositiveSmallIntegerField()
	publishing_date = models.DateTimeField(verbose_name="yayımlanma_tarihi",auto_now_add=True)
	updating_date = models.DateTimeField(verbose_name="yayımlanma_tarihi",auto_now=True)
	filtre1 = models.CharField(max_length=100, default = "-")
	filtre2 = models.CharField(max_length=100, default = "-")
	descriptions = models.CharField(max_length=500, default = "Python Dersleri")
	anahtar = models.CharField(max_length=500, default = "Python Dersleri")
	slug2 = models.SlugField( max_length=130, default = "python")
	#watching_number = models.PositiveSmallIntegerField(default = 0)
	objects = MyManager()
	
	def __str__(self):
		return self.headline
	
	class Meta:
		ordering = ['number']
	
	def get_absolute_url(self):
		return reverse('ingilizce:detail', kwargs={'slug':self.slug, 'slug2':self.slug2})

	def hreflang_get_absolute_url(self):
		if self.number < 76:
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
		all_lessons = Lesson.objects.all()
		all_lessons = list(all_lessons)
		ranking = all_lessons.index(self)
		if self == Lesson.objects.last():
			return all_lessons[0].get_absolute_url()
		
		else:
			return all_lessons[ranking + 1].get_absolute_url()

	def previous_lesson(self):
		all_lessons = Lesson.objects.all()
		all_lessons = list(all_lessons)
		ranking = all_lessons.index(self)
		if self == Lesson.objects.first():
			return all_lessons[-1].get_absolute_url()
		
		else:
			return all_lessons[ranking - 1].get_absolute_url()
	
	def set_number(self):
		for i in Lesson.objects.filter(number__gte = self.number):
			i.number = i.number + 1
			i.save()
	
	def delete_number(self):
		for i in Lesson.objects.filter(number__gte = self.number):
			print(i)
			i.number = i.number - 1
			i.save()