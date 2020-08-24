from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Iletisim(models.Model):
	isim = models.CharField(max_length=100)
	email = models.EmailField()
	content = models.TextField(verbose_name = "Mesajınız")
	publishing_date = models.DateTimeField(verbose_name="yayımlanma_tarihi",auto_now_add=True)
	
	def __str__(self):
		return self.isim

	class Meta:
		ordering = ['publishing_date']