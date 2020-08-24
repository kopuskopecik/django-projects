from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect
from django.views.generic import CreateView, UpdateView, DetailView, ListView, TemplateView
from django.contrib import messages

from braces.views import LoginRequiredMixin

from .models import Lesson
from .forms import LessonForm

from hakkimizda.forms import IletisimForm
from hakkimizda.models import Iletisim

class HeaderMixin():
# Burası view sınıfları ile ilgili metotları override edeceğimiz yer. Buradan miras inheritance yapan
# tüm viewlerde aynı durumlar gözlenir.
	@property
	def action(self):
		msg = "{0} is missing action.".format(self.__class__)
		raise NotImplementedError(msg)
		
	def form_valid(self, form):
		msg = "Lesson {0}!".format(self.action)
		messages.info(self.request, msg)
		return super(HeaderMixin, self).form_valid(form)
	
	def get_context_data(self, **kwargs):
		context = super(HeaderMixin, self).get_context_data(**kwargs)
		
		
		genel1 = Lesson.objects.general1()
		genel2 = Lesson.objects.general2()
		moduller = Lesson.objects.modules()
		paketler1 = Lesson.objects.packet1()
		paketler2 = Lesson.objects.packet2()
		
		context["genel1"] = genel1
		context["genel2"] = genel2
		context["moduller"] = moduller
		context["paketler1"] = paketler1
		context["paketler2"] = paketler2
		
		return context	

class LessonIndexView(HeaderMixin, ListView):
	template_name = 'ingilizce/index.html'
	context_object_name = 'lessons'
	
	def get_queryset(self):
		return Lesson.objects.filter(filtre2__contains = "ana")
	
	
class AnaIndexView(HeaderMixin, ListView):
	template_name = 'ingilizce/ana_index.html'
	context_object_name = 'lessons'
	
	def get_queryset(self):
		return get_list_or_404(Lesson, slug2=self.kwargs['slug2'])

class LessonAllIndexView(HeaderMixin, ListView):
	template_name = 'ingilizce/all_lesson.html'
	context_object_name = 'lessons'
	
	def get_queryset(self):
		q = self.request.GET.get("q")
		if q:
			matching = Lesson.objects.filter(headline__icontains=q)
			if matching:
				return matching
			else:
				matching = Lesson.objects.filter(content__icontains = q).distinct() 
				if matching:
					return matching
				else:
					return []
		return Lesson.objects.all() 

class LessonDetailView(HeaderMixin, DetailView):
    model = Lesson
    template_name = 'ingilizce/detail.html'
	
    def get_context_data(self, **kwargs):
        context = super(LessonDetailView, self).get_context_data(**kwargs)
        
        common = Lesson.objects.filter(slug2 = self.kwargs['slug2'])
        # other_lessons = Lesson.objects.exclude(slug = self.kwargs['slug']).filter(filtre2__contains = "ana").filter(number__gte = self.kwargs['number'])[0:6]
        context["common_lessons"] = common
        return context
		


class LessonCreateView(LoginRequiredMixin, HeaderMixin, CreateView):
	model = Lesson
	template_name = 'ingilizce/form.html'
	action = "created"
	
	# Explicitly attach the FlavorForm class
	form_class = LessonForm
	
	
class LessonUpdateView(LoginRequiredMixin, HeaderMixin, UpdateView):
	model = Lesson
	template_name = 'ingilizce/form.html'
	action = "updated"
	
	# Explicitly attach the FlavorForm class
	form_class = LessonForm

class LessonTemplateView(HeaderMixin, CreateView):
	model = Iletisim
	action = "about"
	template_name = 'ingilizce/about.html'
	form_class = IletisimForm

def ing_delete(request, slug, slug2):
	if not request.user.is_authenticated:
		return Http404()
		
	lesson = get_object_or_404(Lesson, slug=slug)
	lesson.delete()
	lesson.delete_number()
	return redirect("ingilizce:index")