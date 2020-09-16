from django.shortcuts import render
from .forms import UserProfileForm,UserUpdateFormCollege,Job,JobUpdationForm,JobCreationForm
from .models import CollegeUserProfile
from django.contrib.auth.decorators import login_required
from django.views.generic import UpdateView, DeleteView

# Create your views here.
@login_required
def createprofile(request):
	if request.method == "POST":
		form = UserProfileForm(request.POST)
		if form.is_valid():
			userprofile = form.save(commit=False)
			userprofile.user = request.user
			userprofile.save()
			return render(request, "college_app/thanks.html")  # return page after filling userinfo form

		else:
			return "#########"

	else:
		form = UserProfileForm()
		return render(request, "college_app/userprofileform.html", {"form": form})
@login_required
def profile(request):


	if request.method == 'POST':
		c_form = UserUpdateFormCollege(request.POST, instance=request.user)

		if c_form.is_valid():
			c_form.save()
			return render(request, 'college_app/update_success.html')
	else:
		c_form = UserUpdateFormCollege(instance=request.user)
	context = {
		'c_form': c_form,

	}
	return render(request, 'college_app/profile.html', context)


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
			return render(request, "college_app/job_detail.html", context)  # return page after posting a new job
			pass
		else:
			pass
		pass
	else:
		form = JobCreationForm()
		return render(request, "college_app/createjob.html", {"form": form})
		pass


@login_required
def job_detail(request, pk=None):
	job = Job.objects.get(pk=pk)
	context={}
	context['job'] = job
	return render(request, "college_app/job_detail.html", context)

class Update_job(UpdateView):
	model = Job
	fields = (
	"job_title", "job_vacancies", "company_name", "job_salary", "type_of_job", "job_location", "job_requirements",
	"job_info", "date", "work_choice")
	template_name = 'college_app/createjob.html'

	def form_valid(self, form):
		form.instance.posted_by = self.request.user
		return super().form_valid(form)

class Delete_job(DeleteView):
	model = Job
	success_url = '/'
@login_required
def posted_jobs(request):
	jobs = request.user.college_jobs.all()
	context = {
		"jobs": jobs,
		"count": len(jobs),
	}
	return render(request, "college_app/posted_jobs.html", context)

