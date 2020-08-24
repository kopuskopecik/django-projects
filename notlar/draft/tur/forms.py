from django import forms
from .models import Dersler

class DerslerForm(forms.ModelForm):
	
	class Meta:
		model = Dersler
		fields = [
			'headline',
			'content',
			'number',
			'filtre1',
			]