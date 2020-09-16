from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views
from . import views


app_name = 'applicant'

urlpatterns = [
    path("create-applicant-user-profile/", views.createprofile, name = "create_applicant_profile"),
    path("jobs-list", views.listjobs, name= "jobs_list"),
    path("job-detail/<int:pk>", views.job_detail, name = "job_detail"),
    path("applytojob/<int:pk>", views.applytojob, name = "applytojob"),
    path('activate/<uid>/<token>/', views.activate, name='activate'),
    path("job_search", views.job_search, name = "job_search"),
    path("job_alert", views.job_alert, name = "job_alert"),
    path("job_recommendations", views.job_recommendations, name = "job_recommendations"),
    path("job_companies", views.job_companies, name = "job_companies"),
    path("career_guidance", views.career_guidance, name = "career_guidance"),
    path("interview_tips", views.interview_tips, name = "interview_tips"),
    path("expert_call", views.expert_call, name = "expert_call"),
    path("matching_job", views.matching_job, name = "matching_job"),
    path("<int:pk>/view_profile/",views.view_profile,name="view_profile"),
    path('<int:pk>/edit_profile/', views.edit_profile, name='edit_profile'),
    path("search", views.search, name = "search"),
    # path('login/', auth_views.LoginView.as_view(),name='login'),
    # path('logout/', auth_views.LogoutView.as_view(), name="logout"),
    # path('recruiter-signup/', views.RecruiterSignUp.as_view(), name="recruiter-signup"),
    # path('applicant-signup/', views.ApplicantSignUp.as_view(), name="applicant-signup"),
    # path('change-password/', auth_views.PasswordChangeView.as_view(template_name = "accounts/password_change_form.html", success_url = reverse_lazy("accounts:password_change_done")), name = "password_change"),
    # path('change-password/done/', auth_views.PasswordChangeDoneView.as_view(template_name = "accounts/password_change_done.html"), name = "password_change_done"),
    

]
