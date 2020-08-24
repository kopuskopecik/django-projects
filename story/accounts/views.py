from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, UpdateView, TemplateView
from django.contrib.auth import login


from .forms import TeacherSignUpForm, StudentSignUpForm
from .models import User


class SignUpView(TemplateView):
    template_name = 'accounts/signup.html'

class TeacherSignUpView(CreateView):
    model = User
    form_class = TeacherSignUpForm
    template_name = 'accounts/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'teacher'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class StudentSignUpView(CreateView):
    model = User
    form_class = StudentSignUpForm
    template_name = 'accounts/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'student'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('profiles:ogrenci_profil', ogrenci_id = user.id)

