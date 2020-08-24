from django import forms
from accounts.models import Student, Etkinlik



class HedefForm(forms.Form):
	hedef = forms.IntegerField(label='Hedef')


class EtkinlikOlusturForm(forms.ModelForm):
	#sınıf_adı = forms.CharField(label='Sınıf Adı')
	class Meta:
		model = Etkinlik
		fields = [
			'isim',
			'sinif_adi',
			'hedef',
			'odul',
			]