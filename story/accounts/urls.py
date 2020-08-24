from django.urls import include, path

from .views import StudentSignUpView, TeacherSignUpView, SignUpView


app_name = "accounts"
urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    #path('signup/', SignUpView.as_view(), name='signup'),
    path('signup/student/', StudentSignUpView.as_view(), name='student_signup'),
    #path('signup/teacher/', TeacherSignUpView.as_view(), name='teacher_signup'),
]