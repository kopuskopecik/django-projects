from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect, HttpResponseRedirect
from django.views.generic import CreateView, UpdateView, DetailView, ListView, TemplateView
from django.contrib import messages

from braces.views import LoginRequiredMixin

from .models import Lesson, Topic
from .forms import LessonForm, AramaFormu

from hakkimizda.forms import IletisimForm
from hakkimizda.models import Iletisim	

def home_view(request):
	basliklar = Topic.objects.filter(modul_mu = True, aktif = True)
	
	context = {
		"basliklar": basliklar,
	}
	return render(request,'ingilizce/home.html', context)

def ing_index(request):
	basliklar = Topic.objects.filter(aktif = True)
	context = {
		"basliklar": basliklar,
	}
	
	return render(request, 'ingilizce/index.html', context)
	
#def django_index(request):
#	baslik = get_object_or_404(Topic, sıra = 1)
#	context = {
#		"baslik": baslik,
#	}
#	
#	return render(request, 'tur/baslik_index.html', context)

def tkinter_index(request):
	baslik = get_object_or_404(Topic, sıra = 2)
	context = {
		"baslik": baslik,
	}
	
	return render(request, 'ingilizce/baslik_index.html', context)

def modul_index(request):
	basliklar = get_list_or_404(Topic, modul_mu = True, aktif = True)
	context = {
		"basliklar": basliklar,
	}
	
	return render(request, 'ingilizce/modul-index.html', context)

def baslik_index(request, slug):	
	
	baslik = get_object_or_404(Topic, slug = slug, aktif = True)
	
	context = {
		"baslik": baslik,
	}
	
	return render(request, 'ingilizce/baslik_index.html', context)

def ing_detail(request, slug, slug2):

			
	baslik = get_object_or_404(Topic, slug = slug2, aktif = True)
	lesson = get_object_or_404(Lesson, slug=slug, baslık = baslik, aktif = True)
	lessons = Lesson.objects.filter(baslık = baslik, aktif = True)
	
	session_key = 'viewed_topic_{}'.format(lesson.pk)
	if not request.session.get(session_key, False):
		lesson.views += 1
		lesson.save(update_fields = ['views'])
		request.session[session_key] = True
	
	
	context = {
		#'hreflang': hreflang,
		'lesson': lesson,
		'lessons': lessons,
		#'next_lesson': next_lesson,
		#'previous_lesson': previous_lesson,
		#'other_lessons': other_lessons,
		'baslik' : baslik,
	}
	return render(request,'ingilizce/yeni-detail.html',context)	

def ing_ara(request):
	
	form = AramaFormu(request.GET or None)
	query = request.GET.get('q')
	if query:
		query = query.replace("I", "ı").replace("İ", "i").lower()
		b = Lesson.objects.filter(headline__icontains = query, aktif = True).distinct()
		if b:
			context = {
			'form': form,
			'b':b,
			}
			return render(request, 'ingilizce/form.html', context)
		else:
			b = Lesson.objects.filter(content__icontains = query, aktif = True).distinct()
			if b:
				context = {
				'b':b,
				'form': form,
				}
				return render(request, 'ingilizce/form.html', context)
	context = {
		'form': form,	
	}
	
	return render(request, 'ingilizce/form.html', context)


def ing_create(request):
	if not request.user.is_superuser:
		return Http404()
	son_ders = Lesson.objects.all().last()
	
	form = LessonForm(request.POST or None)
	if form.is_valid():
		lesson=form.save()
		messages.success(request, "Yeni Ders Başarılı Bir Şekilde Oluşturuldu.",extra_tags="mesaj-basarili")
		if lesson.aktif and lesson.baslık.aktif:
			return HttpResponseRedirect(lesson.get_absolute_url())
		else:
			return redirect('ingilizce:create')
		#return redirect('tur:create')
	context = {
		'form':form,
		'son_ders': son_ders,
	}

	return render(request, 'tur/form.html',context)
	
def ing_update(request, slug, slug2):
	if not request.user.is_superuser:
		return Http404()
		
	lesson = get_object_or_404(Lesson, slug=slug)
	form = LessonForm(request.POST or None, instance=lesson)
	if form.is_valid():
		lesson = form.save()
		messages.success(request, "Ders Başarılı Bir Şekilde Değiştirildi.")
		if lesson.aktif and lesson.baslık.aktif:
			return HttpResponseRedirect(lesson.get_absolute_url())
		else:
			return redirect('ingilizce:create')
		
	context = {
		'form':form,
	}
	return render(request, 'tur/form.html',context)

def ing_delete(request, slug, slug2):
	if not request.user.is_authenticated:
		return Http404()
		
	lesson = get_object_or_404(Lesson, slug=slug)
	lesson.delete()
	lesson.delete_number()
	return redirect("ingilizce:index")