from django import forms

from lessons.models import Baslik, Ders


class DersForm(forms.ModelForm):
	
	
	class Meta:
		model = Ders
		fields = ('baslik', 'title', 'content', 'youtube_urli', 'ranking',)
	
	
	def __init__(self, user, elma, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['baslik'].queryset = Baslik.objects.filter(owner= user)
		print(elma)