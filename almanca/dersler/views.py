from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views.generic import (CreateView, DeleteView, DetailView, ListView, UpdateView)
from django.contrib import messages
from django.forms import inlineformset_factory
from django.db import transaction
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.db.models import Prefetch

import random


from .models import Baslik, Ders, Question, Answer, TakenQuiz, TakenBaslikQuiz
from .forms import BaslikForm, BaseDersInlineFormSet, DersForm, QuestionForm, BaseAnswerInlineFormSet, TakeQuizForm, BaslikOlusturmaFormu, TakeBaslikForm


def anasayfa(request):
	basliklar = Baslik.objects.values("pk", "title", "owner__username", "views", "favori_sayisi", "begenilme_sayisi")
	#basliklar = Baslik.objects.all()
	#print(basliklar)
	context = {
		'basliklar': basliklar,
	}
	return render(request, 'home.html', context)

def baslik_listesi(request):

	basliklar = Baslik.objects.all()
	context = {
		'basliklar': basliklar,
	}
	return render(request, 'dersler/index.html', context)

def baslik_detail(request, pk):
	baslik = get_object_or_404(Baslik.objects.select_related("owner"), pk=pk)
				
	user = baslik.owner
	sahip_mi = user == request.user
	#dersler = Ders.objects.filter(baslik = baslik)
	#dersler = baslik.ders_set.all()
	dersler = baslik.ders_set.all().prefetch_related(
				Prefetch('question_set', queryset = Question.objects.all(), to_attr = "sorular"),
				)
	soru_var_mi = False
	
	for ders in dersler:
		if ders.sorular:
			soru_var_mi = True
	
	session_key = 'viewed_topic_{}'.format(pk)
	if not request.session.get(session_key, False):
		baslik.views += 1
		baslik.save(update_fields = ['views'])
		request.session[session_key] = True
	
	context = {
		'baslik': baslik,
		'dersler': dersler,
		'sahip_mi': sahip_mi,
		'soru_var_mi': soru_var_mi,
	}
	
	return render(request, 'dersler/baslik_detail.html', context)
	
@method_decorator([login_required], name='dispatch')
class BaslikOlusturView(CreateView):
    model = Baslik
    #fields = ('title', 'content', 'ranking', 'youtube_urli',)
    template_name = 'dersler/baslik_ekle.html'
    form_class = BaslikOlusturmaFormu

    def form_valid(self, form):
        baslik = form.save(commit=False)
        user = self.request.user
        baslik.owner = user
        baslik.save()
        messages.success(self.request, 'Baslık başarıyla oluşturulmuştur.')
        return redirect('profil:ogrenci_profil', user.pk)
		
@method_decorator([login_required], name='dispatch')
class BaslikUpdateView(UpdateView):
    model = Baslik
    #fields = ('title', 'content', 'ranking',)
    form_class = BaslikOlusturmaFormu
    context_object_name = 'baslik'
    template_name = 'dersler/baslik_guncelleme_formu.html'
	
    def get_context_data(self, **kwargs):
        dersler = self.get_object().ders_set.all()
        kwargs['dersler'] = dersler
        return super().get_context_data(**kwargs)
		
    def get_queryset(self):
        '''
        This method is an implicit object-level permission management
        This view will only match the ids of existing quizzes that belongs
        to the logged in user.
        '''
        return Baslik.objects.filter(owner = self.request.user)

    def get_success_url(self):
        return reverse('dersler:baslik_guncelle', kwargs={'pk': self.object.pk})
		
@method_decorator([login_required], name='dispatch')
class BaslikDeleteView(DeleteView):
    model = Baslik
    context_object_name = 'baslik'
    template_name = 'dersler/baslik_silme_onaylama.html'
    success_url = reverse_lazy('dersler:baslik_listesi')

    def delete(self, request, *args, **kwargs):
        baslik = self.get_object()
        messages.success(request, 'Başlık %s başarıyla silinmiştir.' % baslik.title)
        return super().delete(request, *args, **kwargs)
	
    def get_queryset(self):
        return Baslik.objects.filter(owner = self.request.user)

 		
@login_required
def ders_ekle(request, baslik_pk):
    # By filtering the quiz by the url keyword argument `pk` and
    # by the owner, which is the logged in user, we are protecting
    # this view at the object-level. Meaning only the owner of
    # quiz will be able to add questions to it.
    baslik = get_object_or_404(Baslik.objects.select_related("owner"), pk=baslik_pk, owner=request.user)

    if request.method == 'POST':
        form = DersForm(request.POST)
        if form.is_valid():
            ders = form.save(commit=False)
            ders.baslik = baslik
            ders.save()
            messages.success(request, 'Başarı bir şekilde ders eklendi')
            return redirect(baslik)
    else:
        form = DersForm()

    return render(request, 'dersler/ders_ekle_formu.html', {'baslik': baslik, 'form': form})
	
@login_required
def ders_degistir(request, baslik_pk, ders_pk):
    #baslik = get_object_or_404(Baslik.objects.select_related("owner"), pk=baslik_pk, owner=request.user)
    ders = get_object_or_404(Ders.objects.select_related("baslik", "baslik__owner"), pk=ders_pk, baslik__owner=request.user, baslik__id = baslik_pk)
    baslik = ders.baslik
	
    DersFormSet = inlineformset_factory(
        Baslik,  # parent model
        Ders,  # base model
        formset=BaseDersInlineFormSet,
        fields=('title', 'content', 'ranking'),
        min_num=1,
        validate_min=True,
        max_num=10,
        validate_max=True
    )

    if request.method == 'POST':
        form = BaslikOlusturmaFormu(request.POST, instance=baslik)
        formset = DersFormSet(request.POST, instance=baslik)
        if form.is_valid() and formset.is_valid():
            with transaction.atomic():
                form.save()
                formset.save()
            messages.success(request, 'Baslik ve Dersler başarıyla oluşturuldu!')
            return redirect('dersler:baslik_guncelle', baslik.pk)
    else:
        form = BaslikOlusturmaFormu(instance=baslik)
        formset = DersFormSet(instance=baslik)

    return render(request, 'dersler/baslik_degistirme_formu.html', {
        'baslik': baslik,
		'ders': ders,
        'form': form,
        'formset': formset
    })
	
@login_required
def ders_sil(request, pk):
	ders = get_object_or_404(Ders.objects.select_related("baslik", "baslik__owner"), pk=pk, baslik__owner = request.user)
	ders.delete()
	messages.success(request, "Ders Başarılı Bir Şekilde Silindi")
	return redirect(ders.baslik)

@login_required
def ders_guncelle(request, baslik_pk, ders_pk):
	ders = get_object_or_404(Ders.objects.select_related("baslik", "baslik__owner"), pk=ders_pk, baslik__owner=request.user, baslik__id = baslik_pk)
	baslik = ders.baslik		
	
	sorular = ders.question_set.all()
	
	
	form = DersForm(request.POST or None, instance=ders)
	if form.is_valid():
		ders = form.save()
		messages.success(request, "Ders Başarılı Bir Şekilde Değiştirildi.")
		return redirect(ders.baslik)
		
	context = {
		'form':form,
		'ders':ders,
		'sorular': sorular,
		'baslik':baslik,
	}
	return render(request, 'dersler/ders_guncelleme_formu.html',context)


@login_required
def soru_ekle(request, baslik_pk, ders_pk):
    # By filtering the quiz by the url keyword argument `pk` and
    # by the owner, which is the logged in user, we are protecting
    # this view at the object-level. Meaning only the owner of
    # quiz will be able to add questions to it.
    ders = get_object_or_404(Ders.objects.select_related("baslik", "baslik__owner"), pk=ders_pk, baslik__owner=request.user, baslik__id = baslik_pk)
    baslik = ders.baslik

    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            soru = form.save(commit=False)
            soru.ders = ders
            soru.save()
            messages.success(request, 'Soru Başarıyla Oluşturuldu')
            return redirect(ders)
    else:
        form = QuestionForm()

    return render(request, 'dersler/soru_ekle_formu.html', {'baslik': baslik, 'form': form, 'ders':ders})

@login_required
def soru_sil(request, pk):
	soru = get_object_or_404(Question.objects.select_related("ders"), pk=pk, ders__baslik__owner = request.user)
	soru.delete()
	messages.success(request, "Soru Başarılı Bir Şekilde Silindi")
	return redirect(soru.ders)

@login_required
def sorulara_cevap_ekle(request, baslik_pk, ders_pk, soru_pk):
    soru = get_object_or_404(Question.objects.select_related("ders__baslik__owner", ), pk= soru_pk, ders__pk=ders_pk, ders__baslik__owner=request.user, ders__baslik__id = baslik_pk)
    ders = soru.ders
    baslik = ders.baslik
	
	#baslik = get_object_or_404(Baslik, pk=baslik_pk, owner=request.user)
    #ders = get_object_or_404(Ders, pk=ders_pk, baslik=baslik)
    #soru = get_object_or_404(Question, ders=ders, pk = soru_pk)

    AnswerFormSet = inlineformset_factory(
        Question,  # parent model
        Answer,  # base model
        formset=BaseAnswerInlineFormSet,
        fields=('content', 'dogru_cevap'),
        min_num=2,
        validate_min=True,
        max_num=10,
        validate_max=True
    )

    if request.method == 'POST':
        form = QuestionForm(request.POST, instance=soru)
        formset = AnswerFormSet(request.POST, instance=soru)
        if form.is_valid() and formset.is_valid():
            with transaction.atomic():
                form.save()
                formset.save()
            messages.success(request, 'Soru ve Cevaplar başarıyla oluşturuldu!')
            return redirect('dersler:ders_guncelle', baslik.pk, ders.pk)
    else:
        form = QuestionForm(instance=soru)
        formset = AnswerFormSet(instance=soru)

    return render(request, 'dersler/sorulara_cevap_ekleme_formu.html', {
        'baslik': baslik,
		'ders': ders,
        'form': form,
        'formset': formset,
		'soru': soru,
    })
	

def take_quiz(request, pk):
    quiz = get_object_or_404(Ders, pk=pk)
    student = request.user.student

    total_questions = quiz.question_set.count()
    unanswered_questions = student.get_unanswered_questions(quiz)
    total_unanswered_questions = unanswered_questions.count()
    progress = 100 - round(((total_unanswered_questions - 1) / total_questions) * 100)
    question = unanswered_questions.first()

    if request.method == 'POST':
        form = TakeQuizForm(question=question, data=request.POST)
        if form.is_valid():
            with transaction.atomic():
                student_answer = form.save(commit=False)
                student_answer.student = student
                student_answer.save()
                if student.get_unanswered_questions(quiz).exists():
                    return redirect('dersler:take_quiz', pk)
                else:
                    correct_answers = student.studentanswer_set.filter(answer__question__ders=quiz, answer__dogru_cevap=True).count()
                    score = round((correct_answers / total_questions) * 100.0, 2)
                    TakenQuiz.objects.create(student=student, quiz=quiz, score=score)
                    if score < 50.0:
                        messages.warning(request, 'Sonraki Sefer için İyi Şanslar.%s için puanınız %s.' % (quiz.title, score))
                    else:
                        messages.success(request, 'Congratulations! You completed the quiz %s with success! You scored %s points.' % (quiz.title, score))
                    all_answers = student.studentanswer_set.all()
                    all_answers.delete()
                    return redirect('home')
    else:
        form = TakeQuizForm(question=question)

    return render(request, 'dersler/take_quiz_form.html', {
        'quiz': quiz,
        'question': question,
        'form': form,
        'progress': progress
    })

@login_required	
def take_baslik_quiz(request, pk):
    baslik = get_object_or_404(Baslik, pk=pk)
    student = request.user.student
         	
    questions = Question.objects.filter(ders__baslik = baslik)
    total_questions = questions.count()
	
    unanswered_questions = student.get_unanswered_baslik_questions(baslik, questions)
    #print("\n", unanswered_questions, "\n")
    total_unanswered_questions = unanswered_questions.count()
    progress = 100 - round(((total_unanswered_questions - 1) / total_questions) * 100)
    #question = random.choice(unanswered_questions)
    #print(question)
    question = unanswered_questions.first()
    dogru_cevap = question.dogru_cevabi_getir()
    if request.method == 'POST':
        form = TakeBaslikForm(question=question, data=request.POST)
        if form.is_valid():
            with transaction.atomic():
                student_answer = form.save(commit=False)
                student_answer.student = student
                student_answer.save()
                if student.get_unanswered_baslik_questions(baslik, questions).exists():
                    return redirect('dersler:take_baslik_quiz', pk)
                else:
                    correct_answers = student.studentbaslikanswer_set.filter(answer__question__ders__baslik=baslik, answer__dogru_cevap=True).count()
                    score = round((correct_answers / total_questions) * 100.0, 2)
                    TakenBaslikQuiz.objects.create(student=student, baslik=baslik, score=score)
                    messages.success(request, 'Congratulations! You completed the quiz %s with success! You scored %s points.' % (baslik.title, score))
                    all_answers = student.studentbaslikanswer_set.all()
                    all_answers.delete()
                    return redirect(baslik)
    else:
        form = TakeBaslikForm(question=question)

    return render(request, 'dersler/take_baslik_quiz_form.html', {
        'baslik': baslik,
        'question': question,
        'form': form,
        'progress': progress,
		'dogru_cevap':dogru_cevap,
    })

def alistirma_yap(request, pk):
	baslik = get_object_or_404(Baslik.objects.all(), pk=pk) 
	#sorular = Question.objects.filter(ders__baslik__owner = user).select_related("ders", "ders__baslik").prefetch_related("answer_set")
	dersler = baslik.ders_set.all().prefetch_related("question_set__answer_set")
	sorular = []
	for ders in dersler:
		sorular += [soru for soru in ders.question_set.all()]
		
	#sorular = sorular[0:1]
	sorular = sorular
	context = {
		'sorular': sorular,
		#'ogrenci_id': ogrenci_id,
		#'active': "active",
		#'sahip_mi': sahip_mi,
		'baslik': baslik,
	}
	
	return render(request, 'dersler/alistirma_yap.html', context)

@login_required	
def alistirma_sonucu_hesapla(request, pk):
	baslik = get_object_or_404(Baslik, pk=pk)
	
	ogrenci = request.user.student
	favoriler = ogrenci.favoriler.all()
	
	if TakenBaslikQuiz.objects.filter(baslik__pk = baslik.pk, student = ogrenci).exists():
		takenbaslikquiz = get_object_or_404(TakenBaslikQuiz, baslik__pk=pk, student = ogrenci)
		takenbaslikquiz.score+= 1
		takenbaslikquiz.save()
	else:
		TakenBaslikQuiz.objects.create(baslik = baslik, student = ogrenci, score = 1)
	
	
	
	bilgi = request.GET.get("data")
	print("")
	print("alistirma sonucu hesaplandı")
	print("")
	
	return redirect(baslik)
	

