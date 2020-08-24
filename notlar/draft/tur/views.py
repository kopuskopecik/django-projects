from django.shortcuts import render
from django.urls import reverse
from django.shortcuts import get_object_or_404, render, Http404, redirect, HttpResponseRedirect, get_list_or_404
from tur.models import Dersler
from .forms import DerslerForm
from django.contrib import messages

from ingilizce.models import Lesson

# Create your views here.
def tur_index(request):

	genel1 = Dersler.objects.filter(filtre2 = "ana1")
	genel2 = Dersler.objects.filter(filtre2 = "ana2")
	moduller = Dersler.objects.filter(filtre2 = "ana3")
	paketler1 = Dersler.objects.filter(filtre2 = "ana4")
	paketler2 = Dersler.objects.filter(filtre2 = "ana5")
	
	query = request.GET.get('q')
	if query:
		query = query.replace("I", "ı").replace("İ", "i").lower()
		b = Dersler.objects.filter(headline__icontains = query).distinct()
	#print(query, type(query))
		if b:
			context = {
			'b':b,
			'genel1':genel1,
			'genel2':genel2,
			'moduller':moduller,
			'paketler1':paketler1,
			'paketler2':paketler2,
			}
			return render(request, 'searching.html', context)
		else:
			b = Dersler.objects.filter(content__icontains = query).distinct()
			if b:
				context = {
				'b':b,
				'genel1':genel1,
				'genel2':genel2,
				'moduller':moduller,
				'paketler1':paketler1,
				'paketler2':paketler2,
				}
				return render(request, 'searching.html', context)	
	
	lessons = Dersler.objects.all()
	lesson1 = get_object_or_404(Dersler, number=1)
	
	context = {
		'lessons':lessons,
		'lesson1':lesson1,
		'genel1':genel1,
		'genel2':genel2,
		'moduller':moduller,
		'paketler1':paketler1,
		'paketler2':paketler2,
	}
	
	return render(request, 'tur/index.html', context)
	
def ana_index(request, slug2):

	genel1 = Dersler.objects.filter(filtre2 = "ana1")
	genel2 = Dersler.objects.filter(filtre2 = "ana2")
	moduller = Dersler.objects.filter(filtre2 = "ana3")
	paketler1 = Dersler.objects.filter(filtre2 = "ana4")
	paketler2 = Dersler.objects.filter(filtre2 = "ana5")
	
	query = request.GET.get('q')
	if query:
		query = query.replace("I", "ı").replace("İ", "i").lower()
		b = Dersler.objects.filter(headline__icontains = query).distinct()
	#print(query, type(query))
		if b:
			context = {
			'b':b,
			'genel1':genel1,
			'genel2':genel2,
			'moduller':moduller,
			'paketler1':paketler1,
			'paketler2':paketler2,
			}
			return render(request, 'searching.html', context)
		else:
			b = Dersler.objects.filter(content__icontains = query).distinct()
			if b:
				context = {
				'b':b,
				'genel1':genel1,
				'genel2':genel2,
				'moduller':moduller,
				'paketler1':paketler1,
				'paketler2':paketler2,
				}
				return render(request, 'searching.html', context)	
	
	lessons = get_list_or_404(Dersler, slug2=slug2)
	
	context = {
		'lessons':lessons,
		'genel1':genel1,
		'genel2':genel2,
		'moduller':moduller,
		'paketler1':paketler1,
		'paketler2':paketler2,
	}
	
	return render(request, 'tur/ana_index.html', context)

def tur_detail(request, slug, slug2):
	#print(request)
	#print("request.sessioN_DATE: {}".format(request.session.get_expiry_date()))
	
	genel1 = Dersler.objects.filter(filtre2 = "ana1")
	genel2 = Dersler.objects.filter(filtre2 = "ana2")
	moduller = Dersler.objects.filter(filtre2 = "ana3")
	paketler1 = Dersler.objects.filter(filtre2 = "ana4")
	paketler2 = Dersler.objects.filter(filtre2 = "ana5")
	
	query = request.GET.get('q')
	if query:
		query = query.replace("I", "ı").replace("İ", "i").lower()
		b = Dersler.objects.filter(headline__icontains = query).distinct()
	#print(query, type(query))
		if b:
			context = {
			'b':b,
			'genel1':genel1,
			'genel2':genel2,
			'moduller':moduller,
			'paketler1':paketler1,
			'paketler2':paketler2,
			}
			return render(request, 'searching.html', context)
		else:
			b = Dersler.objects.filter(content__icontains = query).distinct()
			if b:
				context = {
				'b':b,
				'genel1':genel1,
				'genel2':genel2,
				'moduller':moduller,
				'paketler1':paketler1,
				'paketler2':paketler2,
				}
				return render(request, 'searching.html', context)	
	
	lesson = get_object_or_404(Dersler, slug=slug)
	lessons = Dersler.objects.filter(filtre1 = lesson.filtre1)
	other_lessons = Dersler.objects.exclude(slug = slug).filter(filtre2__contains = "ana").filter(number__gte = lesson.number)[0:6]
	if lesson== Dersler.objects.last():
		next_lesson = get_object_or_404(Dersler, number=1)
	else:
		next_lesson = get_object_or_404(Dersler, number= lesson.number + 1)
	
	if lesson== Dersler.objects.first():
		previous_lesson = get_object_or_404(Dersler, number=Dersler.objects.last().number)
	else:
		previous_lesson = get_object_or_404(Dersler, number= lesson.number - 1)
			
	if lesson.number < 76:
		if Lesson.objects.filter(number = lesson.number).exists():
			href_lesson = Lesson.objects.get(number = lesson.number)
			
			hreflang = reverse('ingilizce:detail', kwargs={'slug':href_lesson.slug, 'slug2':href_lesson.slug2})
		else:
			hreflang = reverse('ingilizce:index')
	
	else:
		hreflang = reverse('ingilizce:index')
	
	
	context = {
		'hreflang': hreflang,
		'lesson': lesson,
		'lessons': lessons,
		'next_lesson': next_lesson,
		'previous_lesson': previous_lesson,
		'other_lessons': other_lessons,
		'genel1':genel1,
		'genel2':genel2,
		'moduller':moduller,
		'paketler1':paketler1,
		'paketler2':paketler2,
	}
	return render(request,'tur/detail.html',context)

def tur_create(request):
	if not request.user.is_authenticated:
		return Http404()
		
	genel1 = Dersler.objects.filter(filtre2 = "ana1")
	genel2 = Dersler.objects.filter(filtre2 = "ana2")
	moduller = Dersler.objects.filter(filtre2 = "ana3")
	paketler1 = Dersler.objects.filter(filtre2 = "ana4")
	paketler2 = Dersler.objects.filter(filtre2 = "ana5")
	
	query = request.GET.get('q')
	if query:
		query = query.replace("I", "ı").replace("İ", "i").lower()
		b = Dersler.objects.filter(headline__icontains = query).distinct()
	#print(query, type(query))
		if b:
			context = {
			'b':b,
			'genel1':genel1,
			'genel2':genel2,
			'moduller':moduller,
			'paketler1':paketler1,
			'paketler2':paketler2,
			}
			return render(request, 'searching.html', context)
		else:
			b = Dersler.objects.filter(content__icontains = query).distinct()
			if b:
				context = {
				'b':b,
				'genel1':genel1,
				'genel2':genel2,
				'moduller':moduller,
				'paketler1':paketler1,
				'paketler2':paketler2,
				}
				return render(request, 'searching.html', context)	
	
	form = DerslerForm(request.POST or None)
	if form.is_valid():
		lesson=form.save()
		messages.success(request, "Yeni Ders Başarılı Bir Şekilde Oluşturuldu.",extra_tags="mesaj-basarili")
		return HttpResponseRedirect(lesson.get_absolute_url())
		#return redirect('tur:create')
	context = {
		'form':form,
		'genel1':genel1,
		'genel2':genel2,
		'moduller':moduller,
		'paketler1':paketler1,
		'paketler2':paketler2,
	}

	return render(request, 'tur/form.html',context)
	
def tur_update(request, slug, slug2):
	if not request.user.is_authenticated:
		return Http404()

	genel1 = Dersler.objects.filter(filtre2 = "ana1")
	genel2 = Dersler.objects.filter(filtre2 = "ana2")
	moduller = Dersler.objects.filter(filtre2 = "ana3")
	paketler1 = Dersler.objects.filter(filtre2 = "ana4")
	paketler2 = Dersler.objects.filter(filtre2 = "ana5")
	
	query = request.GET.get('q')
	if query:
		query = query.replace("I", "ı").replace("İ", "i").lower()
		b = Dersler.objects.filter(headline__icontains = query).distinct()
	#print(query, type(query))
		if b:
			context = {
			'b':b,
			'genel1':genel1,
			'genel2':genel2,
			'moduller':moduller,
			'paketler1':paketler1,
			'paketler2':paketler2,
			}
			return render(request, 'searching.html', context)
		else:
			b = Dersler.objects.filter(content__icontains = query).distinct()
			if b:
				context = {
				'b':b,
				'genel1':genel1,
				'genel2':genel2,
				'moduller':moduller,
				'paketler1':paketler1,
				'paketler2':paketler2,
				}
				return render(request, 'searching.html', context)
		
	lesson = get_object_or_404(Dersler, slug=slug)
	form = DerslerForm(request.POST or None, instance=lesson)
	if form.is_valid():
		form.save()
		messages.success(request, "Ders Başarılı Bir Şekilde Değiştirildi.")
		return HttpResponseRedirect(lesson.get_absolute_url())
		
	context = {
		'form':form,
		'genel1':genel1,
		'genel2':genel2,
		'moduller':moduller,
		'paketler1':paketler1,
		'paketler2':paketler2,
	}
	return render(request, 'tur/form.html',context)

def tur_delete(request, slug, slug2):
	if not request.user.is_authenticated:
		return Http404()
		
	lesson = get_object_or_404(Dersler, slug=slug)
	lesson.delete()
	lesson.delete_number()
	return redirect("tur:index")