from django.urls import path
from django.shortcuts import render
from django.views.generic.base import TemplateView, RedirectView
from django.views.generic.dates import DateDetailView


from .views import MyView, HomePageView, DerslerCounterRedirectView, DerslerDetailView,TemplatePageView, ContactView
from .views import ArticleCreate, ArticleUpdate, ArticleDelete, ArticleArchive, ArticleYearArchiveView, ArticleMonthArchiveView, ArticleWeekArchiveView, ArticleDayArchiveView, ArticleTodayArchiveView
from .models import Article

from django.contrib.flatpages.sitemaps import FlatPageSitemap
from django.contrib.sitemaps.views import sitemap
from django.contrib.sitemaps import GenericSitemap
from django.contrib.sitemaps import views

from home.sitemaps import ArticleSitemap
from .feed import LatestEntriesFeed


info_dict = {
	'queryset': Article.objects.all(),
	'date_field': 'publishing_date',
}

app_name = "denemeler"
urlpatterns = [
    path('mine/', MyView.as_view(), name='my-view'),
	path('template/', TemplatePageView.as_view(extra_context = {'a': "extra keyword"}), name='home'),
	
	#feed
	path('latest/feed/', LatestEntriesFeed()),
	
	# the sitemap
	path('sitemap.xml', sitemap,{'sitemaps': {'flatpages': FlatPageSitemap, 'articles': ArticleSitemap}},name='django.contrib.sitemaps.views.sitemap'),
	path('a/sitemap.xml', sitemap,{'sitemaps': {'article': GenericSitemap(info_dict, priority=0.6)}}, name='django.contrib.sitemaps.views.sitemap.generic'),
	path('sitemap.xml', views.index, {'sitemaps': {'flatpages': FlatPageSitemap, 'articles': ArticleSitemap}}),
	path('sitemap-<section>.xml', views.sitemap, {'sitemaps': {'flatpages': FlatPageSitemap, 'articles': ArticleSitemap}}, name='django.contrib.sitemaps.views.sitemap'),
	
	path('', HomePageView.as_view(extra_context = {'a': "extra keyword"}), name='home'),
	
	path('contact/', ContactView.as_view(), name='contact'),
	
	path('create/', ArticleCreate.as_view(), name='create'),
	path('<slug:slug>/update/', ArticleUpdate.as_view(), name='update'),
	path('<slug:slug>/delete/', ArticleDelete.as_view(), name='delete'),
	
	path('archive/',ArticleArchive.as_view(),name="article_archive"),
	path('<int:year>/',ArticleYearArchiveView.as_view(),name="article_year_archive"),
	# Example: /2012/08/
	path('<int:year>/<int:month>/', ArticleMonthArchiveView.as_view(month_format='%m'),name="archive_month_numeric"),
	# Example: /2012/aug/
	path('<int:year>/<str:month>/',ArticleMonthArchiveView.as_view(),name="archive_month"),
	# Example: /2012/week/23/
	path('<int:year>/hafta/<int:week>/',ArticleWeekArchiveView.as_view(),name="archive_week"),
	# Example: /2012/nov/10/
    path('<int:year>/<str:month>/<int:day>/',ArticleDayArchiveView.as_view(),name="archive_day"),
	#path('<int:year>/<int:month>/<int:day>/',ArticleDayArchiveView.as_view(day_format = "%d"),name="archive_day_numeric"),
	path('today/', ArticleTodayArchiveView.as_view(), name="archive_today"),
	path('<int:year>/<str:month>/<int:day>/<slug:slug>/',DateDetailView.as_view(model=Article, date_field="publishing_date"),name="archive_date_detail"),
	
	path('counter/<int:pk>/', DerslerCounterRedirectView.as_view(), name='article-counter'),
	#path('details/<int:pk>/', DerslerDetail.as_view(), name='article-detail'),
	path('go-to-django/', RedirectView.as_view(url='https://djangoproject.com'),name='go-to-django'),
	path('<slug:slug>/', DerslerDetailView.as_view(), name='article-detail'),
]