from django import forms
from django.forms.utils import ValidationError
from django.utils.safestring import mark_safe
from django.shortcuts import reverse


from .models import Baslik, Ders, Question, Answer, StudentAnswer, StudentBaslikAnswer


class BaseDersInlineFormSet(forms.BaseInlineFormSet):
    def clean(self):
        super().clean()

class BaseAnswerInlineFormSet(forms.BaseInlineFormSet):
    def clean(self):
        super().clean()

        dogru_cevap_sayisi = 0
        has_one_correct_answer = False
        for form in self.forms:
            if not form.cleaned_data.get('DELETE', False):
                if form.cleaned_data.get('dogru_cevap', False):
                    has_one_correct_answer = True
                    break
        if not has_one_correct_answer:
            raise ValidationError('Bir adet doğru cevap olmalıdır.', code='no_correct_answer')
		
        for form in self.forms:
            if form.cleaned_data.get('dogru_cevap') == True:
                dogru_cevap_sayisi += 1 
        if dogru_cevap_sayisi > 1:
            raise ValidationError('Yalnızca bir adet doğru cevap olmalıdır.', code='no_correct_answer')
		
class BaslikForm(forms.ModelForm):
    class Meta:
        model = Baslik
        fields = ('title', 'content', 'ranking',)


class DersForm(forms.ModelForm):
	class Meta:
		model = Ders
		fields = ('title', 'content', 'youtube_urli', 'ranking',)
		
		
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['title'].widget.attrs['placeholder']= "Dersinizin başlığını belirleyiniz"
		self.fields['title'].widget.attrs['class']= "form-control-sm"
		self.fields['content'].widget.attrs['placeholder']= "Dersinizin İçeriği"
		self.fields['content'].widget.attrs['class']= "form-control-sm"
		self.fields['youtube_urli'].widget.attrs['placeholder']= "Bu dersinize yönelik Youtube videosunun linki(zorunlu değil)"
		self.fields['youtube_urli'].widget.attrs['class']= "form-control-sm"
		self.fields['ranking'].widget.attrs['class']= "form-control-sm"	

class QuestionForm(forms.ModelForm):
	class Meta:
		model = Question
		fields = ('content',)
	
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['content'].widget.attrs['placeholder']= "sorunuz"
		self.fields['content'].widget.attrs['class']= "form-control-sm"

class TakeQuizForm(forms.ModelForm):
    answer = forms.ModelChoiceField(
        queryset=Answer.objects.none(),
        widget=forms.RadioSelect(),
        required=True,
        empty_label=None)

    class Meta:
        model = StudentAnswer
        fields = ('answer', )

    def __init__(self, *args, **kwargs):
        question = kwargs.pop('question')
        super().__init__(*args, **kwargs)
        self.fields['answer'].queryset = question.answer_set.order_by('content')
		

		
class TakeBaslikForm(forms.ModelForm):
    answer = forms.ModelChoiceField(
        queryset=Answer.objects.none(),
        widget=forms.RadioSelect(),
        required=True,
        empty_label=None)

    class Meta:
        model = StudentBaslikAnswer
        fields = ('answer', )

    def __init__(self, *args, **kwargs):
        question = kwargs.pop('question')
        super().__init__(*args, **kwargs)
        self.fields['answer'].queryset = question.answer_set.all()	
	



class BaslikOlusturmaFormu(forms.ModelForm):
	
	class Meta:
		model = Baslik
		fields = ('title', 'content', 'youtube_urli', 'ranking',)
		
		
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['title'].widget.attrs['placeholder']= "Dersleriniz için bir genel başlık belirleyiniz"
		self.fields['title'].widget.attrs['class']= "form-control-sm"
		self.fields['content'].widget.attrs['placeholder']= "Başlığınızın genel olarak ne içereceğini burda belirtebilirsiniz."
		self.fields['content'].widget.attrs['class']= "form-control-sm"
		self.fields['youtube_urli'].widget.attrs['placeholder']= "Başlık altında yer almasını istediğiniz Youtube videosunun linki"
		self.fields['youtube_urli'].widget.attrs['class']= "form-control-sm"
		self.fields['ranking'].widget.attrs['class']= "form-control-sm"		