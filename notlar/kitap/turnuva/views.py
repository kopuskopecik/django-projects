from django.shortcuts import render, get_object_or_404, redirect

from accounts.models import Student, Etkinlik
from accounts.forms import StudentSignUpForm

from .forms import HedefForm, EtkinlikOlusturForm
from accounts.models import User, Teacher

# Create your views here.

def ogretmen(request, teacher_id):
	ogretmen = get_object_or_404(Teacher, pk = teacher_id)

	context = {
		'teacher_id': teacher_id,
		'ogretmen': ogretmen,
		#'form': form,
	}
	
	return render(request,'turnuva/ogretmen.html', context)

def etkinlik_olustur(request, teacher_id):
	ogretmen = get_object_or_404(Teacher, pk = teacher_id)
	if request.method == 'POST':
		# create a form instance and populate it with data from the request:
		form = EtkinlikOlusturForm(request.POST)
		# check whether it's valid:
		if form.is_valid():
			etkinlik = form.save(commit = False)
			etkinlik.ogretmen = ogretmen
			etkinlik.save()
			#student = Student.objects.create(student=user, teacher = request.user.teacher)
			#sinif.ogrenci.add(student)
			return redirect('anasayfa:anasayfa')
			# if a GET (or any other method) we'll create a blank form
	else:
		form = EtkinlikOlusturForm()
	
	context = {
		'form': form,
	}
	
	return render(request,'turnuva/etkinlik.html',context)
	
def etkinliklerim(request, teacher_id):
	ogretmen = get_object_or_404(Teacher, pk = teacher_id)
	etkinlikler = ogretmen.etkinlik_set.all()
	context = {
		'ogretmen': ogretmen,
		'etkinlikler': etkinlikler,
	}

	return render(request,'turnuva/etkinliklerim.html', context)

def etkinlik_detail(request, teacher_id, etkinlik_id):
	ogretmen = get_object_or_404(Teacher, pk = teacher_id)
	etkinlik = get_object_or_404(Etkinlik, pk = etkinlik_id, ogretmen = ogretmen)

	context = {
		'ogretmen': ogretmen,
		"etkinlik": etkinlik,
	}

	return render(request,'turnuva/etkinlik-detail.html', context)

def ogrenciler(request, teacher_id, etkinlik_id):
	ogretmen = get_object_or_404(Teacher, pk = teacher_id)
	etkinlik = get_object_or_404(Etkinlik, pk = etkinlik_id, ogretmen = ogretmen)
	ogrenciler = etkinlik.ogrenci.all()
	print(ogrenciler)

	context = {
		'ogretmen': ogretmen,
		"etkinlik": etkinlik,
		"ogrenciler": ogrenciler,
	}

	return render(request,'turnuva/ogrenciler.html', context)



