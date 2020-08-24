from django.http import HttpResponse
from django.views import View, generic
from django.views.generic.base import TemplateView, RedirectView
from django.shortcuts import render
from django.utils import timezone
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.views.generic.dates import ArchiveIndexView, YearArchiveView, MonthArchiveView, WeekArchiveView, DayArchiveView, TodayArchiveView
from django.urls import reverse_lazy
from django.contrib.auth import get_user
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator

from tur.models import Dersler
from .models import Article
from .forms import ContactForm, ArticleForm


class MyView(View):
	def get(self, request, *args, **kwargs):
		dersler = Dersler.objects.all()[0:10]
		
		print("")
		print(get_user(request))
		print("")
		#print(dersler)
		context = {
			'dersler': dersler,
		}
		return render(request, 'denemeler/index.html', context)

class TemplatePageView(TemplateView):
	template_name = "denemeler/home.html"
	
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['articles'] = Article.objects.all()
		
		return context


class HomePageView(generic.ListView):
	template_name = "denemeler/home.html"
	model = Article
	context_object_name = "articles"
	ordering = "-publishing_date"
	#queryset = Article.objects.filter(name__icontains= "l")
	#paginate_by = 3 # if pagination is desired
	#page_kwarg = "sayfa"
	#paginate_orphans = 1
	
	def __init__(self, **kwargs):
		a = super().__init__(**kwargs)
		print("")
		#print(a)
		#print(kwargs)
		return super().__init__(**kwargs)
	
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['now'] = timezone.now()
		context['sayı1'] = 5
		context['sayı2'] = 150000005
		context['sayı3'] = 1234567890
		print("")
		#print(context)
		return context
		
	def dispatch(self, request, *args, **kwargs):
		print("")
		#print(request)
		print("")
		#print(args)
		print("")
		#a = messages.add_message(request, messages.INFO, 'Hello world.')
		#print(a)
		messages.add_message(request, messages.SUCCESS, 'Profile details updated.',fail_silently=True,)
		messages.info(request, 'Hello world.', fail_silently=True)
		#messages.set_level(request, messages.WARNING)
		messages.info(request, 'Three credits remain in your account.', "deneme")
		messages.success(request, 'Profile details updated.')
		messages.warning(request, 'Your account expires in three days.')
		messages.error(request, 'Document deleted.')
		current_level = messages.get_level(request)
		print(current_level)
		#CRITICAL = 50
		#messages.add_message(request, CRITICAL, 'A serious error occurred.')
		for i in messages.get_messages(request):
			print(type(i))
		print(messages.get_messages(request))
		#print(kwargs)
		
		return super().dispatch(request, *args, **kwargs)
	
	def render_to_response(self, context, **response_kwargs):
		"""
		Return a response, using the `response_class` for this view, with a
		template rendered with the given context.
		Pass response_kwargs to the constructor of the response class.
		"""
		print("")
		#print(context)
		print("")
		#print(response_kwargs)
		print("")
		#print(self.request)
		print("")
		#print(self.get_template_names())
		print("")
		#print(self.template_engine)
		
		response_kwargs.setdefault('content_type', self.content_type)
		return self.response_class(
        request=self.request,
        template=self.get_template_names(),
        context=context,
        using=self.template_engine,
        **response_kwargs
		)

		
class DerslerCounterRedirectView(RedirectView):
	permanent = False
	query_string = True
	pattern_name = 'denemeler:article-detail'
	# url = "/"
	
	def get_redirect_url(self, *args, **kwargs):
		print("")
		print(args)
		print("")
		print(kwargs)
		print("")
		print(self.request.META.get('QUERY_STRING', ''))
		#ders = get_object_or_404(Dersler, pk=kwargs['pk'])
		#ders.update_counter()
		return super().get_redirect_url(*args, **kwargs)
		#return reverse(self.pattern_name, args = args, kwargs = kwargs)

class DerslerDetailView(generic.DetailView):
	model = Article
	#context_object_name = 'artikel'
	template_name = "denemeler/detail.html"
	extra_context = {'a': 'Ekstra içerik'}
	#queryset = Article.objects.exclude(name = "Siyaset")
	#queryset = Dersler.objects.all()	
	#template_name_suffix = "_detay"
	template_name_field = "name"
	
	def get_context_data(self, **kwargs):
		#print(self.pk_url_kwarg)
		print("")
		#print(kwargs)
		context = super().get_context_data(**kwargs)
		print("")
		#print(context)
		print(self.object.slug)
		context['now'] = timezone.now()
		return context
	
	def get(self, request, *args, **kwargs):
		print("")
		#print(self.kwargs)
		print("")
		#print(self.args)
		#print(kwargs)
		print("")
		#print(request)
		
		print("")
			
		return super().get(request, *args,**kwargs)
		
	def get_context_object_name(self, obj):
		print("")
		#print(obj._meta.model_name)
		#print(dir(obj))
		#print("get context içi:  ", self.kwargs, self.request, self.args)
		print(self.object.slug)
		return super().get_context_object_name(obj)
		
		
	def get_object(self, queryset = None):
		#print(self.queryset)
		return super().get_object(queryset)
		#return Dersler.objects.get(id = 1)
	
	def dispatch(self, request, *args, **kwargs):
		print("")
		#print(request)
		print("")
		#print(args)
		print("")
		#print(kwargs)
		
		return super().dispatch(request, *args, **kwargs)


class ContactView(FormView):
	template_name = 'denemeler/contact.html'
	form_class = ContactForm
	success_url = 'denemeler:home'
	#initial = {'name': "Merhaba", 'message': "Televole"}
	prefix = "deneme"
	def form_valid(self, form):
# This method is called when valid form data has been POSTed.
# It should return an HttpResponse.
		form.send_email()
		return super().form_valid(form)
		
	def form_invalid(self, form):
		"""If the form is invalid, render the invalid form."""
		print(form)
		return self.render_to_response(self.get_context_data(form=form))
		


class ArticleCreate(SuccessMessageMixin, CreateView):
	model = Article
	fields = ['name', 'slug', 'user']
	success_message = "%(slug)s was created successfully"
	#form_class = ArticleForm
	
	def form_valid(self, form):
		"""If the form is valid, save the associated model."""
		print("")
		print(form)
		print("")
		print(type(form))
		self.object = form.save()
		print("")
		print(type(self.object))
		print("")
		print(self.object.get_absolute_url())
		print("")
		print(dir(self.object))
		return super().form_valid(form)


class ArticleUpdate(UpdateView):
    model = Article
    fields = ['name']
	#success_url="/polls/{slug}/"
    #template_name_suffix = '_update_form'


class ArticleDelete(DeleteView):
    model = Article
    success_url = reverse_lazy('denemeler:home')
    #success_url = '/denemeler/'


class ArticleArchive(ArchiveIndexView):
	model= Article 
	date_field="publishing_date"
	#date_list_period = 'day'


class ArticleYearArchiveView(YearArchiveView):
	queryset = Article.objects.all()
	date_field = "publishing_date"
	#year = "2020"
	#year_format = "%y"
	make_object_list = True
	allow_future = True
	
	def _get_current_year(self, date):
		"""Return the start date of the current interval."""
		a = super()._get_current_year(date)
		print("get_current_year")
		#print(date.replace(month=1, day=1))
		print(date)
		print(a)
		return a
	
	def get_next_year(self, date):
		a = super().get_next_year(date)
		print("next")
		print(date)
		print(a)
		"""Get the next valid year."""
		#return _get_next_prev(self, date, is_previous=False, period='year')
		return a

	def get_previous_year(self, date):
		a = super().get_previous_year(date)
		print("previous")
		print(date)
		print(a)
		"""Get the next valid year."""
		#return _get_next_prev(self, date, is_previous=False, period='year')
		return a
	
	def get_year(self):
		a = super().get_year()
		print("year")
		print(a)
		return a
	
class ArticleMonthArchiveView(MonthArchiveView):
	queryset = Article.objects.all()
	date_field = "publishing_date"
	allow_future = True


class ArticleWeekArchiveView(WeekArchiveView):
	queryset = Article.objects.all()
	date_field = "publishing_date"
	week_format = "%W"
	allow_future = True


class ArticleDayArchiveView(DayArchiveView):
	queryset = Article.objects.all()
	date_field = "publishing_date"
	allow_future = True



class ArticleTodayArchiveView(TodayArchiveView):
	queryset = Article.objects.all()
	date_field = "publishing_date"
	allow_future = True	



















		
		
		
		
		
		
		