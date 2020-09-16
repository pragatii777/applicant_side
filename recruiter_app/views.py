from django.shortcuts import render, get_object_or_404
from .forms import UserProfileForm, JobCreationForm, UserUpdateForm
from .models import RecruiterUserProfile, Job,Short_list_candidate
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.views.generic import UpdateView, DeleteView
from django import forms
from django.conf import settings
from django.core.mail import send_mail
from applicant_app.models import ApplicantUserProfile
from django.db.models import Q
from django.db.models import F
from django.shortcuts import redirect


# Create your views here.

@login_required
def createprofile(request):
	if request.method == "POST":
		form = UserProfileForm(request.POST)
		if form.is_valid():
			userprofile = form.save(commit=False)
			userprofile.user = request.user
			userprofile.save()
			return render(request, "recruiter_app/thanks.html")  # return page after filling userinfo form

		else:
			return "#########"

	else:
		form = UserProfileForm()
		return render(request, "recruiter_app/userprofileform.html", {"form": form})


@login_required
def createjob(request):
	if request.method == "POST":
		form = JobCreationForm(request.POST)
		if form.is_valid():
			job = form.save(commit=False)
			job.posted_by = request.user
			job.save()
			context = {
				"job": job,
			}
			context['job'] = job
			return render(request,"recruiter_app/job_detail.html",context)  # return page after posting a new job
			pass
		else:
			pass
		pass
	else:
		form = JobCreationForm()
		return render(request, "recruiter_app/createjob.html", {"form": form})
		pass


@login_required
def applytojob(request, pk):
	job = Job.objects.get(pk=pk)

	# If User has already applied redirect User to already applied page.
	if request.user in job.applied_by.all():
		return render(request, "recruiter_app/apllication_done_already.html")

	# If User has not applied
	else:
		job.applied_by.add(request.user)
		# job.save()
		n_applications = job.applied_by.count()
		context = {  # Sending number of application to that job in the context
			"n_applications": n_applications
		}
		return render(request, "recruiter_app/application_done.html", context)


@login_required
def removeapplication(request, pk):
	job = Job.objects.get(pk=pk)

	# Validate if the User has applied in the first place
	if request.user not in job.applied_by.all():
		return render(request, "recruiter_app/application_not_done.html")

	# If the User has applied to the job, we can remove the application
	else:
		job.applied_by.remove(request.user)
		n_applications = job.applied_by.count()
		context = {  # Sending number of application to that job in the context
			"n_applications": n_applications
		}
		return render(request, "recruiter/application_removed.html", context)


@login_required
def posted_jobs(request):
	"""
	View to fetch and display the list of jobs posted by a recruiter.
	"""
	jobs = request.user.jobs.all()

	context = {
		"jobs": jobs,
		"count": len(jobs),
	}
	return render(request, "recruiter_app/posted_jobs.html", context)


def job_detail(request, pk=None):
    job = Job.objects.get(pk=pk)
    result = job.job_requirements
    mn = ApplicantUserProfile.objects.all()
    oo = ApplicantUserProfile.objects.none()
    z = []
    for mm in mn:
        jk = mm.area_of_expertise
        r1 = jk.split(',')
        for x in result:
            for y in r1:
                if x == y:
                    z.append(mm.user)
    for ui in z:
        i = ApplicantUserProfile.objects.filter(user=ui)
        oo |= i
    qs1 = job.applied_by.all()
    p = ApplicantUserProfile.objects.none()
    q = ApplicantUserProfile.objects.none()
    for k in qs1:
        qs2 = ApplicantUserProfile.objects.filter(user=k)
        p |= qs2
    q |= oo.exclude(pk__in=p)
    q |= q
    context = {
			'job': job,
			'qs': q,
			'count': len(q),
			'count1': len(p),
			'qs1': p,
		}
    context['job'] = job
    return render(request, "recruiter_app/job_detail.html", context)


class Update_job(UpdateView):
    model=Job

    fields = ("job_title", "job_vacancies","company_name", "job_salary","type_of_job","job_location","job_requirements","job_info","date","work_choice")
    template_name='recruiter_app/createjob.html'
    def form_valid(self,form):
        form.instance.posted_by=self.request.user
        return super().form_valid(form)




class Delete_job(DeleteView):
	model = Job
	success_url = '/'
k=6
prof="50%"

@login_required
def profile(request):
	global k,prof

	if request.method == 'POST':

		u_form = UserUpdateForm(request.POST, instance=request.user)
		if u_form.data['designation']:
			k = k + 1
		if u_form.data['location']:
			k = k + 1
		if u_form.data['url_of_company']:
			k = k + 1
		if u_form.data['why_join_us']:
			k = k + 1
		if u_form.data['company_description']:
			k = k + 1

		if k == 7:
			prof = "60%"
		elif k == 8:
			prof = "70%"
		elif k == 9:
			prof = "80%"
		elif k == 10:
			prof = "90%"
		elif k == 11:
			prof = "100%"

		if u_form.is_valid():
			u_form.save()
			return render(request, 'recruiter_app/update_success.html')
	else:
		u_form = UserUpdateForm(instance=request.user)
	context = {
		'u_form': u_form,
		'prof': prof,
	}
	prof = "50%"
	k = 6

	return render(request, 'recruiter_app/profile.html', context)


@login_required
def my_candidates(request):
	"""
	View to fetch and display the list of jobs posted by a recruiter.
	"""
	jobs = request.user.jobs.all()

	context = {
		"jobs": jobs,
		"count": len(jobs),
	}
	return render(request, "recruiter_app/my_candidates.html", context)
@login_required
def search_candidates(request):
	m=ApplicantUserProfile.objects.all()
	query=""
	context={}
	if request.GET:
		query=request.GET['q']
		context={
			'query':str(query)
		}
	m=get_queryset(query)


	context={
		'm':m
	}
	return render(request, "recruiter_app/search_candidates.html", context)
def get_queryset(query=None):
	queryset=[]
	queries=query.split(" ")
	for ji in queries:
		candidates=ApplicantUserProfile.objects.filter(
			Q(area_of_expertise__icontains=ji) |
			Q(location__icontains=ji) |
			Q(industry__icontains=ji)
		).distinct()
		for can in candidates:
			queryset.append(can)
	return list(set(queryset))

def job_matching(request, pk=None):
    job = Job.objects.get(pk=pk)
    result = job.job_requirements
    mn=ApplicantUserProfile.objects.all()
    oo=ApplicantUserProfile.objects.none()
    z=[]
    for mm in mn:
        jk=mm.skill_info
        for x in result:
            for y in jk:
                if x==y:
                    z.append(mm.user)
    for ui in z:
            i=ApplicantUserProfile.objects.filter(user=ui)
            oo |= i
    qs1 = job.applied_by.all()
    p = ApplicantUserProfile.objects.none()
    q = ApplicantUserProfile.objects.none()
    for k in qs1:
        qs2 = ApplicantUserProfile.objects.filter(user=k)
        p |= qs2
    q |= oo.exclude(pk__in=p)
    q |= q
    nn=Short_list_candidate.objects.none()
    for aa in q:
        n=Short_list_candidate.objects.filter(candidate=aa)
        nn |=n
    l1=[]
    for o in nn:
        l1.append(o.candidate)
    context = {
			'job': job,
			'qs': q,
			'count': len(q),
			'count1':len(p),
			'qs1':p,
		    'nn':l1
    }
    context['job'] = job
    return render(request, "recruiter_app/job_matching.html", context)


def applicant_detail(request, pk=None):
	context = {}
	applicantuserprofile = ApplicantUserProfile.objects.get(pk=pk)
	context['applicantuserprofile'] = applicantuserprofile
	return render(request, "recruiter_app/applicant_detail.html", context)

@login_required
def can(request,pk=None,mk=None):
		job=Job.objects.get(pk=mk)
		Short_listed_candidate = Short_list_candidate()
		if request.method=="GET":
			applicantuserprofile = ApplicantUserProfile.objects.get(pk=pk)
			Short_listed_candidate.candidate = applicantuserprofile
			Short_listed_candidate.save()
			Short_listed_candidate.jobs.add(job.pk)
			Short_listed_candidate.save()
			return redirect(request.META['HTTP_REFERER'])

@login_required
def alreadycan(request,pk=None):
    job=Job.objects.get(pk=pk)
    po=Short_list_candidate.objects.filter(jobs=job)
    following = po.all().values_list('candidate', flat=True)
    queryset = ApplicantUserProfile.objects.filter(pk__in=list(following))
    context={
		'l1':queryset,
		'count':len(queryset)
	}
    return render(request,"recruiter_app/thankyou.html",context)
@login_required
def pricing(request):
	return render(request,"recruiter_app/view_plans.html")
@login_required
def purchase_plan(request):
	return render(request,"recruiter_app/purchase_plan.html")
@login_required
def campus_hiring(request):
	return render(request,"recruiter_app/campus_hiring.html")



@login_required
def assessments(request):
	return render(request,"recruiter_app/assessments.html")



@login_required
def add_a_blog(request):
	return render(request,"recruiter_app/add_a_blog.html")

@login_required
def recruiter_blog(request):
	return render(request,"recruiter_app/recruiter_blog.html")