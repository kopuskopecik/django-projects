from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
	is_student = models.BooleanField(default=False)
	is_teacher = models.BooleanField(default=False)

class Teacher(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
	
class Student(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
	favoriler = models.ManyToManyField('dersler.Baslik')
	quizzes = models.ManyToManyField('dersler.Ders')
	
	
	def get_unanswered_questions(self, quiz):
		answered_questions = self.studentanswer_set.all() \
		.filter(answer__question__ders=quiz) \
		.values_list('answer__question__pk', flat=True)
		questions = quiz.question_set.exclude(pk__in=answered_questions).order_by('content')
		return questions

	def get_unanswered_baslik_questions(self, baslik, questions):
		answered_questions = self.studentbaslikanswer_set.all() \
		.filter(answer__question__ders__baslik=baslik) \
		.values_list('answer__question__pk', flat=True)
		questions = questions.exclude(pk__in=answered_questions)
		print("")
		print("kalan sorular:", questions)
		print("cevaplanan sorular:", answered_questions)
		print("")
		return questions
		
		
	def __str__(self):
		return self.user.username
