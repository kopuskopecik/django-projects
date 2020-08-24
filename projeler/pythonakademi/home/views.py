from django.shortcuts import render, redirect
from tur.models import Dersler, Baslik
from front.models import Baslik as Bas
#import random

# Create your views here.
def home_view(request):
	basliklar = Baslik.objects.filter(modul_mu = True, aktif = True)
	front_basliklar = Bas.objects.filter(modul_mu = True, aktif = True)
	
	context = {
		"basliklar": basliklar,
		"front_basliklar": front_basliklar,
	}
	return render(request,'home.html',context)
	
def view_404(request, exception):
    # make a redirect to homepage
    # you can use the name of url or just the plain link
    return redirect('/')
