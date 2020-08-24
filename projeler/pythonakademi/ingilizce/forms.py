from .models import Lesson
from django import forms

class LessonForm(forms.ModelForm):

	class Meta:
		model = Lesson
		fields = [
			'baslık',
			'headline',
			'content',
			'number',
			'descriptions',
			'anahtar',
			'filtre1',
			'filtre2',
			'aktif',
			]

class AramaFormu(forms.Form):
	q = forms.CharField(label = "Search", max_length=100)