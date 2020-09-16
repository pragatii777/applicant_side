from django import forms
from multiselectfield import MultiSelectFormField
from .models import CollegeUserProfile, ProfcessUser,Job


class UserProfileForm(forms.ModelForm):
	name = forms.CharField(max_length=140, widget=forms.TextInput(attrs={'class': 'form-control'}))
	location = forms.CharField(max_length=140, widget=forms.TextInput(attrs={'class': 'form-control'}))
	designation = forms.CharField(max_length=140, widget=forms.TextInput(attrs={'class': 'form-control'}))
	college_name = forms.CharField(max_length=140, widget=forms.TextInput(attrs={'class': 'form-control'}))
	Url_of_college = forms.CharField(max_length=140, widget=forms.TextInput(attrs={'class': 'form-control'}))
	why_join_us = forms.CharField(max_length=540, widget=forms.TextInput(attrs={'class': 'form-control'}))
	# cell = forms.CharField(max_length=10, widget=forms.TextInput(attrs={'class': 'form-control'}))
	# HR_email = forms.EmailField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
	college_description = forms.CharField(max_length=540, widget=forms.TextInput(attrs={'class': 'form-control'}))

	class Meta:
		model = CollegeUserProfile
		fields = (
		"name", "location", "designation", "college_name", "Url_of_college", "why_join_us", "college_description")

	pass
class UserUpdateFormCollege(forms.ModelForm):
	email = forms.EmailField()
	class Meta:
		model = ProfcessUser
		fields = ['username', 'email', "first_name", "last_name", "phone", "college_name", "designation", "location",
				  "url_of_college", "why_join_us", "college_description", ]
class JobCreationForm(forms.ModelForm):
	job_requirements = forms.MultipleChoiceField(choices=Job.SKILLS)
	class Meta:
		model = Job

		widgets = {
			'work_choice': forms.RadioSelect()
		}
		fields = (
			"job_title", "job_vacancies", "company_name", "job_salary", "type_of_job", "job_location",
			"job_requirements", "job_info",
			"work_choice", "date")

		pass
class JobUpdationForm(forms.ModelForm):
	job_requirements = forms.MultipleChoiceField(choices=Job.SKILLS)
	class Meta:
		model = Job
		widgets = {
			'work_choice': forms.RadioSelect()
		}
		fields = (
			"job_title", "job_vacancies", "company_name", "job_salary", "type_of_job", "job_location",
			"job_requirements", "job_info",
			"work_choice", "date")

	def save(self, commit=True):
		job = self.instance
		job.job_title = self.cleaned_data['job_title']
		job.job_vacancies = self.cleaned_data['job_vacancies']
		job.company_name = self.cleaned_data['company_name']
		job.job_salary = self.cleaned_data['job_salary']
		job.job_info = self.cleaned_data['job_info']
		job.job_requirements = self.cleaned_data['job_requirements']
		job.job_location = self.cleaned_data['job_location']
		job.date = self.cleaned_data['date']
		job.work_choice = self.cleaned_data['work_choice']
		if commit:
			job.save()
		return job