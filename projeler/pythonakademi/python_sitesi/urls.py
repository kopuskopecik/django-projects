"""python_sitesi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import path, include
from django.views.generic import TemplateView
#from django.conf.urls import handler404

from home.views import home_view
from home.sitemaps import DerslerSitemap, LessonSitemap
from home.sitemaps import StaticViewSitemap, TopicSitemap, BaslikSitemap


#handler404 = 'home_view' 

handler404 = 'home.views.view_404'

sitemaps = {
	'static' : StaticViewSitemap,
	'basliklar': BaslikSitemap,
	'topics': TopicSitemap,
	'dersler': DerslerSitemap,
	'lessons': LessonSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
	path('sitemap.xml/', sitemap, {'sitemaps':sitemaps}),
	path('', home_view, name = "home"),
	path('robots.txt/', TemplateView.as_view(template_name="robots.txt", content_type ="text/plain")),
	path('ads.txt/', TemplateView.as_view(template_name="ads.txt", content_type ="text/plain")),
	path('google064e6732d3ae6437.html/', TemplateView.as_view(template_name="google064e6732d3ae6437.html")),
	path('python/', include('tur.urls')),
	path('en/python/', include('ingilizce.urls')),
	path('', include('hakkimizda.urls')),
	path('', include('front.urls')),
	
]
