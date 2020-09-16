from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views
from . import views

app_name = 'accounts'
urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
    path('index/',views.index,name="index"),
    path('recruiter-signup/', views.recruiter_signup, name="recruiter-signup"),
    path('activate/<uid>/<token>/', views.activate, name='activate'),
    path('applicant-signup/', views.ApplicantSignUp, name="applicant-signup"),
    path('college-signup/', views.college_signup, name="college-signup"),
    path('email_form/',views.email_form,name="email_form"),
    path('change-password/', auth_views.PasswordChangeView.as_view(template_name="accounts/password_change_form.html",
                                                                   success_url=reverse_lazy(
                                                                       "accounts:password_change_done")),
         name="password_change"),
    path('change-password/done/',
         auth_views.PasswordChangeDoneView.as_view(template_name="accounts/password_change_done.html"),
         name="password_change_done"),
    path('applicant-signup/privacy.html', views.showprivacy, name="showprivacy"),
    path('applicant-signup/terms.html', views.showterms, name="showterms"),
    path('recruiter-signup/privacy.html', views.showprivacy, name="showprivacy"),
    path('recruiter-signup/terms.html', views.showterms, name="showterms"),
    path('college-signup/privacy.html', views.showprivacy, name="showprivacy"),
    path('college-signup/terms.html', views.showterms, name="showterms"),
    path('about/', views.about, name="about"),
]

