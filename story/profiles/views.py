from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages


from accounts.models import User
from lessons.models import Baslik, Ders, Question
from .forms import DersForm


def ogretmen_profil(request, ogretmen_id):
	basliklar = Baslik.objects.filter(owner = request.user)
	#lessons = Ders.objects.filter(baslik = baslik)
	context = {
		'basliklar': basliklar,
		'ogretmen_id': ogretmen_id,
		'active': "active",
	}
	
	return render(request, 'profiles/ogretmen.html', context)

def ogrenci_profil(request, ogrenci_id):
	user = get_object_or_404(User, pk=ogrenci_id)
	basliklar = user.baslik_set.all().prefetch_related("ders_set")
	#basliklar = Baslik.objects.filter(owner = user).select_related("owner")
	sahip_mi = user == request.user
	#ders_sayisi = basliklar.
	
	context = {
		'basliklar': basliklar,
		'ogrenci_id': ogrenci_id,
		'active': "active",
		'sahip_mi': sahip_mi,
	}
	
	return render(request, 'profiles/ogrenci.html', context)

def favorilere_baslik_ekle(request, baslik_id):
	baslik = get_object_or_404(Baslik, pk=baslik_id)
	favoriler = request.user.student.favoriler
	if favoriler.filter(pk = baslik_id).exists():
		favoriler.remove(baslik)
		if favoriler:
			baslik.favori_sayisi -= 1
			baslik.save(update_fields = ['favori_sayisi'])
	else:
		baslik.favori_sayisi += 1
		baslik.save(update_fields = ['favori_sayisi'])
		favoriler.add(baslik)
		
	return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def begen(request, baslik_id):
	baslik = get_object_or_404(Baslik, pk=baslik_id)
	
	session_key = 'begen_topic_{}'.format(baslik_id)
	if not request.session.get(session_key, False):
		baslik.begenilme_sayisi += 1
		baslik.save(update_fields = ['begenilme_sayisi'])
		request.session[session_key] = True
	
	else:
		baslik.begenilme_sayisi -= 1
		baslik.save(update_fields = ['begenilme_sayisi'])
		request.session[session_key] = False
		
	return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
	
def favoriler(request, ogrenci_id):
	user = get_object_or_404(User.objects.select_related("student"), pk = ogrenci_id)
	basliklar = user.student.favoriler.all().prefetch_related("ders_set")
	#lessons = Ders.objects.filter(baslik = baslik)
	context = {
		'basliklar': basliklar,
		'ogrenci_id': ogrenci_id,
		'active': "active",
	}
	
	return render(request, 'profiles/favoriler.html', context)


def derslerim(request, ogrenci_id):
	user = get_object_or_404(User, pk=ogrenci_id)
	lessons = Ders.objects.filter(baslik__owner = user).select_related("baslik").prefetch_related("question_set")
	sahip_mi = user == request.user
	
	context = {
		'lessons': lessons,
		'ogrenci_id': ogrenci_id,
		'active': "active",
		'sahip_mi': sahip_mi,
	}
	
	return render(request, 'profiles/derslerim.html', context)


def sorular(request, ogrenci_id):
	user = get_object_or_404(User, pk=ogrenci_id)
	sorular = Question.objects.filter(ders__baslik__owner = user).select_related("ders", "ders__baslik").prefetch_related("answer_set")
	sahip_mi = user == request.user
	
	context = {
		'sorular': sorular,
		'ogrenci_id': ogrenci_id,
		'active': "active",
		'sahip_mi': sahip_mi,
	}
	
	return render(request, 'profiles/sorular.html', context)
	
@login_required
def ders_olustur(request, ogrenci_id):
	user = request.user
	ogrenci = get_object_or_404(User, id = ogrenci_id)
	elma = "armut"
	if user == ogrenci:
		if request.method == 'POST':
			form = DersForm(elma = elma, user = request.user, data = request.POST)
			if form.is_valid():
				#baslik = form.cleaned_data['baslik_secimi']
				ders = form.save(commit=False)			
				#ders.baslik = baslik
				ders.save()
				messages.success(request, 'Başarı bir şekilde ders eklendi')
				return redirect(ders.baslik)
		else:
			form = DersForm(request.user, elma = elma)
		return render(request, 'profiles/ders_olustur_formu.html', {'form': form})
	else:
		return HttpResponseNotFound('<h1>Yetkiniz Yok. Lütfen üye olun</h1>')
   
	
	