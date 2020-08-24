from django import forms
from .models import Iletisim
#from captcha.fields import ReCaptchaField

class IletisimForm(forms.ModelForm):
	#captcha = ReCaptchaField()
	class Meta:
		model = Iletisim
		fields = [
			'isim',
			'email',
			'content',			
			]