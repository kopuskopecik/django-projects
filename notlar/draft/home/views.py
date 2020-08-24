from django.shortcuts import render, redirect, HttpResponse
from tur.models import Dersler
#import random

# Create your views here.
def home_view(request):	
	
	print("")
	print("Session Denemeleri")
	print("")
	# Oturumun sona ermes süresini belirler.
	#request.session.set_expiry(2)
	print("request.session: {}".format(request.session.keys()))
	print("request.session: {}".format(request.session.values()))
	print("request.sessioN_DATE: {}".format(request.session.get_expiry_age()))
	print("request.sessioN_DATE: {}".format(request.session.get_expiry_date()))
	#fav_color = request.session['fav_color']
	
	print("")
	
	lessons = Dersler.objects.filter(filtre2__contains = "ana")	
	
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
		
	context = {
		'lessons':lessons,
		'genel1':genel1,
		'genel2':genel2,
		'moduller':moduller,
		'paketler1':paketler1,
		'paketler2':paketler2,
	}
	return render(request,'home.html',context)
	
def view_404(request, exception):
    # make a redirect to homepage
    # you can use the name of url or just the plain link
    return redirect('/')
