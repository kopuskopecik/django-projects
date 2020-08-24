from django import forms
from .models import Article


class ContactForm(forms.Form):
	name = forms.CharField()
	message = forms.CharField(widget=forms.Textarea)
	
	def send_email(self):
	# send email using the self.cleaned_data dictionary
		pass

class ArticleForm(forms.ModelForm):
	message = forms.CharField(widget=forms.Textarea)
	class Meta:
		model  = Article
		fields = ['name','slug', 'user',]


	
	
