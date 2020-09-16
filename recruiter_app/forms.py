from django import forms
from multiselectfield import MultiSelectFormField
from django_select2.forms import Select2MultipleWidget

from .models import RecruiterUserProfile, Job, ProfcessUser,UserData


class UserProfileForm(forms.ModelForm):
	name = forms.CharField(max_length=140, widget=forms.TextInput(attrs={'class': 'form-control'}))
	location = forms.CharField(max_length=140, widget=forms.TextInput(attrs={'class': 'form-control'}))
	designation = forms.CharField(max_length=140, widget=forms.TextInput(attrs={'class': 'form-control'}))
	company_name = forms.CharField(max_length=140, widget=forms.TextInput(attrs={'class': 'form-control'}))
	Url_of_company = forms.CharField(max_length=140, widget=forms.TextInput(attrs={'class': 'form-control'}))
	why_join_us = forms.CharField(max_length=540, widget=forms.TextInput(attrs={'class': 'form-control'}))
	# cell = forms.CharField(max_length=10, widget=forms.TextInput(attrs={'class': 'form-control'}))
	# HR_email = forms.EmailField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
	company_description = forms.CharField(max_length=540, widget=forms.TextInput(attrs={'class': 'form-control'}))

	class Meta:
		model = RecruiterUserProfile
		fields = (
		"name", "location", "designation", "company_name", "Url_of_company", "why_join_us", "company_description")

	pass


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


class DetailUpdateForm(forms.ModelForm):
	class Meta:
		model = RecruiterUserProfile
		fields = ["name", "location", "designation", "company_name", "Url_of_company", "why_join_us",
				  "company_description"]


class UserUpdateForm(forms.ModelForm):
	email = forms.EmailField()

	class Meta:
		model = ProfcessUser
		fields = ['username', 'email', "first_name", "last_name", "phone", "company_name", "designation", "location",
				  "url_of_company", "why_join_us", "company_description", ]

class ProfileUpdateForm(forms.ModelForm):
	class Meta:
		model = UserData
		fields = ['token']
