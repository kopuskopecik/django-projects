from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from tur.models import Dersler, Baslik
from ingilizce.models import Lesson, Topic



class DerslerSitemap(Sitemap):
	protocol = "https"

	def items(self):
		return Dersler.objects.filter(aktif = True)
		
	def lastmod(self, obj):
		return obj.updating_date
		
class LessonSitemap(Sitemap):
	protocol = "https"

	def items(self):
		return Lesson.objects.filter(aktif = True)
		
	def lastmod(self, obj):
		return obj.updating_date

class TopicSitemap(Sitemap):
	protocol = "https"

	def items(self):
		return Topic.objects.filter(aktif = True)

class BaslikSitemap(Sitemap):
	protocol = "https"

	def items(self):
		return Baslik.objects.filter(aktif = True)


class StaticViewSitemap(Sitemap):
	protocol = "https"
	
	def items(self):
		return [
			'hakkimizda:hak', 
			'tur:index', 
			'tur:django-index', 
			'tur:tkinter-index',
			'tur:modul-index',
			'ingilizce:ing-home',
			'ingilizce:index',
			'ingilizce:tkinter-index',
			'ingilizce:modul-index',
		]
	
	def location(self, item):
		return reverse(item)

