from django.shortcuts import render
from django.urls import reverse
from django.shortcuts import get_object_or_404, render, Http404, redirect, HttpResponseRedirect, get_list_or_404
from .models import Dersler, Baslik
from .forms import DerslerForm, AramaFormu
from django.contrib import messages

#from ingilizce.models import Lesson

# Create your views here.


def front_index(request):
	basliklar = Baslik.objects.filter(aktif = True)
	baslik_adi = basliklar.first().get_ana_başlık_display()
	
	context = {
		"basliklar": basliklar,
		'baslik_adi': baslik_adi,
	}
	
	return render(request, 'tur/index.html', context)

	
def baslik_index(request, slug):	
	
	baslik = get_object_or_404(Baslik, slug = slug, aktif = True)
	
	context = {
		"baslik": baslik,
	}
	
	return render(request, 'tur/baslik_index.html', context)

def front_detail(request, slug, slug2):

			
	baslik = get_object_or_404(Baslik, slug = slug2, aktif = True)
	lesson = get_object_or_404(Dersler, slug=slug, baslık = baslik, aktif = True)
	lessons = Dersler.objects.filter(baslık = baslik, aktif = True)
	
	session_key = 'viewed_topic_{}'.format(lesson.pk)
	if not request.session.get(session_key, False):
		lesson.views += 1
		lesson.save()
		request.session[session_key] = True
	
	
	
	context = {
		'lesson': lesson,
		'lessons': lessons,
		#'next_lesson': next_lesson,
		#'previous_lesson': previous_lesson,
		#'other_lessons': other_lessons,
		'baslik' : baslik,
	}
	return render(request,'front/yeni-detail.html',context)

def front_create(request):
	if not request.user.is_superuser:
		return Http404()
	son_ders = Dersler.objects.all().last()
	
	form = DerslerForm(request.POST or None)
	if form.is_valid():
		lesson=form.save()
		messages.success(request, "Yeni Ders Başarılı Bir Şekilde Oluşturuldu.",extra_tags="mesaj-basarili")
		if lesson.aktif and lesson.baslık.aktif:
			return HttpResponseRedirect(lesson.get_absolute_url())
		else:
			return redirect('tur:create')
		#return redirect('tur:create')
	context = {
		'form':form,
		'son_ders': son_ders,
	}

	return render(request, 'tur/form.html',context)
	
def front_update(request, slug, slug2):
	if not request.user.is_superuser:
		return Http404()
		
	lesson = get_object_or_404(Dersler, slug=slug)
	form = DerslerForm(request.POST or None, instance=lesson)
	if form.is_valid():
		lesson = form.save()
		messages.success(request, "Ders Başarılı Bir Şekilde Değiştirildi.")
		if lesson.aktif and lesson.baslık.aktif:
			return HttpResponseRedirect(lesson.get_absolute_url())
		else:
			return redirect('tur:create')
		
	context = {
		'form':form,
	}
	return render(request, 'tur/form.html',context)

def front_delete(request, slug, slug2):
	if not request.user.is_authenticated:
		return Http404()
		
	lesson = get_object_or_404(Dersler, slug=slug)
	lesson.delete()
	lesson.delete_number()
	return redirect("tur:index")
	
def front_ara(request):
	
	form = AramaFormu(request.GET or None)
	query = request.GET.get('q')
	if query:
		query = query.replace("I", "ı").replace("İ", "i").lower()
		b = Dersler.objects.filter(headline__icontains = query, aktif = True).distinct()
		if b:
			context = {
			'form': form,
			'b':b,
			}
			return render(request, 'form.html', context)
		else:
			b = Dersler.objects.filter(content__icontains = query, aktif = True).distinct()
			if b:
				context = {
				'b':b,
				'form': form,
				}
				return render(request, 'form.html', context)
	context = {
		'form': form,	
	}
	
	return render(request, 'form.html', context)
