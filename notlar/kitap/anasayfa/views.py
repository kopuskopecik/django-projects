from django.shortcuts import render, redirect
from django.views import generic

from .models import Genel

from shop.models import Category, Product


class AnaSayfa(generic.ListView):
	model = Category
	template_name = 'anasayfa/anasayfa.html'
	
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		urunler = Product.objects.filter(ogrenci_sayisi = "a")
		genel = Genel.objects.all()
		context["urunler"] = urunler
		context["genel"] = genel
		return context

class GenelDetailView(generic.DetailView):
	model = Genel
	template_name = 'anasayfa/genel-detail.html'

	
	# def get(self, request, *args, **kwargs):
	# 	if request.user.is_authenticated:
	# 		if request.user.is_teacher:
	# 			return redirect('turnuva:ogretmen', request.user.teacher.pk)
	# 		else:
	# 			return redirect('my_account')
	# 	return super().get(request, *args, **kwargs)

#class DetailView(generic.DetailView):
#    model = Question
#    template_name = 'polls/detail.html'