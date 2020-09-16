from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views
from . import views
from recruiter_app.views import job_detail, Update_job,Delete_job,my_candidates,job_matching,search_candidates,campus_hiring,add_a_blog,assessments,recruiter_blog,applicant_detail


app_name = 'recruiter'

urlpatterns = [
    path("create-recruiter-user-profile/",
         views.createprofile, name="create_recruiter_profile"),
    path("profile/",views.profile,name="profile"),
    path("create-job/", views.createjob, name="create_job"),
    path("posted-jobs/", views.posted_jobs, name="posted_jobs"),
    path("job-detail/<int:pk>", views.job_detail, name="job_detail"),
    path("job-detail/<int:pk>/update/", Update_job.as_view(), name = "update_job"),
    path("job-detail/<int:pk>/delete/", Delete_job.as_view(), name = "delete_job"),
    path("search-candidates/",views.search_candidates,name="search_candidates"),
    path("my-candidate/", views.my_candidates, name="my_candidates"),
    path("job-matching/<int:pk>", views.job_matching, name="job_matching"),
    path("campus-hiring/", views.campus_hiring, name="campus_hiring"),
    path("assessments/", views.assessments, name="assessments"),
    path("add-a-blog/", views.add_a_blog, name="add_a_blog"),
    path("recruiter-blog/", views.recruiter_blog, name="recruiter_blog"),
    path("applicant-detail/<int:pk>", views.applicant_detail, name="applicant_detail"),
    path("can/<int:pk>/<int:mk>/",views.can,name="can"),
    path("alreadycan/<int:pk>/",views.alreadycan,name="alreadycan"),
    path("pricing/",views.pricing,name="pricing"),
    path("purchase-plan/",views.purchase_plan,name="purchase-plan")



    # path('login/', auth_views.LoginView.as_view(),name='login'),
    # path('logout/', auth_views.LogoutView.as_view(), name="logout"),
    # path('recruiter-signup/', views.RecruiterSignUp.as_view(), name="recruiter-signup"),
    # path('applicant-signup/', views.ApplicantSignUp.as_view(), name="applicant-signup"),
    # path('change-password/', auth_views.PasswordChangeView.as_view(template_name = "accounts/password_change_form.html", success_url = reverse_lazy("accounts:password_change_done")), name = "password_change"),
    # path('change-password/done/', auth_views.PasswordChangeDoneView.as_view(template_name = "accounts/password_change_done.html"), name = "password_change_done"),


]
