from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField

class Genel(models.Model):
	başlık = models.CharField(max_length= 100)
	slug = models.SlugField(unique=True, max_length=130)
	image = models.ImageField("resim", blank=True, null = True)
	kısa_içerik = RichTextField()
	uzun_içerik = RichTextField()
	
	class Meta:
		verbose_name = 'Genel-Konu'
		verbose_name_plural = 'Genel-Konular'
	
	def __str__(self):
		return self.başlık
	
	def get_absolute_url(self):
		return reverse('anasayfa:genel-detail', kwargs={'slug':self.slug})
