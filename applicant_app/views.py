from django.shortcuts import render, get_object_or_404, redirect
from .forms import UserProfileForm, InputForm, UserProfileUpdationForm
from .models import ApplicantUserProfile
from recruiter_app.models import Job, RecruiterUserProfile
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes,force_text,DjangoUnicodeDecodeError
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from accounts.models import ProfcessUser
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail
from .token import activation_token
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
# Create your views here.

@login_required
def view_profile(request, pk):
    try:
        UserProfileUpdationForm(instance=request.user.applicantuserprofile)
    except ObjectDoesNotExist:
        return redirect("applicant:create_applicant_profile")
    form = UserProfileUpdationForm(instance=request.user.applicantuserprofile)
    args = {'form': form}
    return render(request, "applicant_app/userprofileform.html", args)

@login_required
def createprofile(request):
    if request.method == "POST":
        print("hello")
        form = UserProfileForm(request.POST)
        if form.is_valid():
            userprofile = form.save(commit=False)
            userprofile.user = request.user
            userprofile.save()
            return render(request, "applicant_app/thanks.html") #return page after filling userinfo form

        else:
            return "#########"
        
    else:
        form = UserProfileForm()
        return render(request, "applicant_app/userprofileform.html", {"form":form})


@login_required
def applytojob(request, pk):
    """ Apply to a job  """
    context = {}
    job = Job.objects.get(pk=pk)
    context['job'] = job

    # If User has already applied redirect User to already applied page.
    if request.user in job.applied_by.all():
        return render(request, "applicant_app/applicationdonealready.html", context)

    log_in_user = ProfcessUser.objects.get(username=request.user.username)
    # if user is already activated then apply to job and show confiramtion
    if log_in_user.activated:
        # user object is is added to job with job id = pk
        job.applied_by.add(request.user)
        messages.success(request, 'Your application is received Recuiter will contact u soon')
        return render(request, "applicant_app/applytojob.html", context)
    else:
        # else send to index page where pop to verify email is shown
        return render(request, "applicant_app/verifyemailfirst.html", context)

@login_required
def listjobs(request):
    """
    Return a list of all jobs.

    """
    jobs = Job.objects.all()
    context = {
        "jobs":jobs
    }

    return render(request, "applicant_app/jobs_list.html", context)

@login_required
def job_detail(request, pk):
    
    job = get_object_or_404(Job, pk=pk)
    context = {
        "job":job,
    }
    
    return render(request, "applicant_app/job_detail.html", context)

@login_required
def mail(request):
        sub = forms.applicant_app()
        fullname = request.POST['fullname']
        mail = request.POST['mail']
        contact = request.POST['contact']
        recipient = str(sub['email'].value())
        send_mail('Verification', 'Applied successfully', 'contact@profcess.com', [recipient], fail_silently=False)
        return render(request,'applicant_app/mail.html')

def search(request):
    jobs = Job.objects.all()
    query_title=request.GET['query_title']
    query_skills=request.GET['query_skills']
    query_location=request.GET['query_location']
    if query_title != '' and  query_title is not None:
        jobs = Job.objects.filter(job_title__icontains=query_title)
    elif query_skills != '' and  query_skills is not None: 
        jobs = Job.objects.filter(job_requirements__icontains=query_skills)
    elif query_location != '' and  query_location is not None: 
        jobs = Job.objects.filter(job_location__icontains=query_location)

    context ={
        "jobs": jobs
    }
    return render(request, 'applicant_app/search.html',context)

def job_search(request):
    jobs = Job.objects.all()
    return render(request,"applicant_app/job_search.html",{'jobs':jobs})
@login_required
def matching_job(request):

    jobs={i:i.applied_by.count() for i in Job.objects.all()}
    sort_orders = sorted(jobs.items(), key=lambda x: x[1], reverse=True)
    my_context=[]
    for i in sort_orders:
        l1=list(i[0].job_requirements)
        l2=list(ApplicantUserProfile.objects.get(user=request.user).skill_info)
        if (all(x in l2 for x in l1)):
            my_context.append({'name':i[0]})
    return render(request,"applicant_app/matching_job.html",context={'jobs':my_context})


@login_required
def job_alert(request):
    return render(request,"applicant_app/job_alert.html")

@login_required
def job_recommendations(request):
    return render(request,"applicant_app/job_recommendations.html")

def job_companies(request):
    recruiter = RecruiterUserProfile.objects.all()
    return render(request,"applicant_app/job_companies.html",{'recruiter':recruiter})

@login_required
def career_guidance(request):
    return render(request,"applicant_app/career_guidance.html")

@login_required
def interview_tips(request):
    return render(request,"applicant_app/interview_tips.html")

@login_required
def expert_call(request):
    return render(request,"applicant_app/expert_call.html")


@login_required
def activate(request,uid,token):    #goes via mail
    return render(request,"applicant_app/activation.html")

@login_required
def edit_profile(request, pk):
    user = ProfcessUser.objects.get(id=pk)
    try:
        UserProfileUpdationForm(instance=request.user.applicantuserprofile)
    except ObjectDoesNotExist:
        return redirect("applicant:create_applicant_profile")
    form= UserProfileUpdationForm(instance=request.user.applicantuserprofile)
    if request.method == "POST":
        print("hello")
        form = UserProfileUpdationForm(request.POST, instance= request.user.applicantuserprofile)
        if form.is_valid():
            form.save()
            return render(request, "applicant_app/thanks.html")

    args = {'form': form}
    return render(request, 'applicant_app/userprofileform.html', args)

# @login_required
# def edit_profile(request, pk):
#     #user = User.objects.get(ApplicantUserProfile, pk=pk)
#     if request.method == "POST":
#         form = UserProfileForm(request.POST, instance=request.user)
#         if form.is_valid():
#             form.save()
#             #return redirect(('applicant:view_profile'))
#             return render(request, "applicant_app/thanks.html")


#     else:
#         form = UserProfileUpdationForm(instance=request.user)
#         context = {'form': form,}
#         return render(request, 'applicant_app/userprofileform.html', context)