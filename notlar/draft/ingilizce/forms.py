from .models import Lesson
from django import forms

class LessonForm(forms.ModelForm):

	class Meta:
		model = Lesson
		fields = [
			'headline',
			'content',
			'number',
			'descriptions',
			'anahtar',
			'filtre1',
			'filtre2'
			]