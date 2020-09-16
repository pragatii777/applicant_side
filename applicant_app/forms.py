from django import forms
from multiselectfield import MultiSelectFormField
from .models import ApplicantUserProfile

year=[tuple([x,x]) for x in range(1980,2020)]
class UserProfileForm(forms.ModelForm):
    # preferred_domain = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    skill_info = forms.MultipleChoiceField(choices=ApplicantUserProfile.SKILLS,required=False)
    class Meta:
        model = ApplicantUserProfile
        fields = ("headline","first_name","last_name","pheadline","current_position","education","country_region","location",
        "industry","contact_information","description","school_name","school_degree","field_of_study","location_of_school",
        "start_school","end_school","experience_title","company_name","company_location","start_company",
        "end_company", "area_of_expertise",
        "project_name","start_project","end_project","project_creator","associated_with",
        "project_url","project_description",
        "accomplishment_title","accomplishment_associated_with","issuer","issue_date","accomplishment_description","skill_info")
    pass

class UserProfileUpdationForm(forms.ModelForm):
    skill_info = forms.MultipleChoiceField(choices=ApplicantUserProfile.SKILLS,required=False)
    class Meta:
        model = ApplicantUserProfile
        fields = ("headline","first_name","last_name","pheadline","current_position","education","country_region","location",
        "industry","contact_information","description","school_name","school_degree","field_of_study","location_of_school",
        "start_school","end_school","experience_title","company_name","company_location","start_company",
        "end_company", "area_of_expertise",
        "project_name","start_project","end_project","project_creator","associated_with",
        "project_url","project_description",
        "accomplishment_title","accomplishment_associated_with","issuer","issue_date","accomplishment_description","skill_info")
    pass

class InputForm(forms.Form):

    fullname = forms.CharField(max_length = 200)
    mail = forms.EmailField()
    contact = forms.IntegerField()