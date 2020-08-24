from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from tur.models import Dersler
from ingilizce.models import Lesson
from denemeler.models import Article 



class DerslerSitemap(Sitemap):
	protocol = "https"
	i18n = True

	def items(self):
		return Dersler.objects.all()
		
	def lastmod(self, obj):
		return obj.updating_date
		



class StaticViewSitemap(Sitemap):
	protocol = "https"
	
	def items(self):
		return ['hakkimizda:hak', 'tur:index']
	
	def location(self, item):
		return reverse(item)

class StaticDerslerViewSitemap(Sitemap):
	protocol = "https"
	
	
	def items(self):
		liste = []
		for i in Dersler.objects.filter(filtre2__contains = "ana"):
			liste.append(i.slug2)
		liste = list(set(liste))
		
		return liste
		
	def location(self, item):
		return "/python/" + item + "/"

class LessonSitemap(Sitemap):
	protocol = "https"
	i18n = True

	def items(self):
		return Lesson.objects.all()[0:76]
		
	def lastmod(self, obj):
		return obj.updating_date

		

class ArticleSitemap(Sitemap):
	changefreq = "never"
	priority = 0.5
	i18n = True

	def items(self):
		return Article.objects.all()

	def lastmod(self, obj):
		return obj.publishing_date