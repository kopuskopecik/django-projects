from django.shortcuts import render
from django.shortcuts import get_object_or_404, render, Http404, redirect, HttpResponseRedirect
from tur.models import Dersler
from .models import Iletisim
from .forms import IletisimForm
from django.contrib import messages

# Create your views here.
def hakkimizda(request):

	a = "hakkimizda"

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
			'a':a,
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
	
	form = IletisimForm(request.POST or None)
	if form.is_valid():
		ileti=form.save()
		messages.success(request, "Mesajınız başarı ile alınmıştır. En kısa zamanda sizinle iletişime geçilecektir.",extra_tags="mesaj-basarili")
		#return HttpResponseRedirect(kelime.get_absolute_url())
		return redirect('hakkimizda:hak')
	context = {
		'form':form,
		'genel1':genel1,
		'genel2':genel2,
		'moduller':moduller,
		'paketler1':paketler1,
		'paketler2':paketler2,
	}
	
	return render(request,'hakkimizda/hakkimizda.html', context)