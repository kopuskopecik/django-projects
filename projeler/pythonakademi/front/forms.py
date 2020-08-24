from django import forms
from .models import Dersler

class DerslerForm(forms.ModelForm):
	
	class Meta:
		model = Dersler
		fields = [
			'baslık',
			'headline',
			'content',
			'number',
			'descriptions',
			'anahtar',
			'aktif',
			]

class AramaFormu(forms.Form):
	q = forms.CharField(label = "Ara", max_length=100)