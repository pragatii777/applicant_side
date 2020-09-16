from django.db import models
from django.core.validators import MaxLengthValidator, MinLengthValidator
from multiselectfield import MultiSelectField
from Profcess_Dev.settings import AUTH_USER_MODEL
User = AUTH_USER_MODEL

# Create your models here.



class ApplicantUserProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        limit_choices_to={"usertype": "Applicant"},
        related_name="applicantuserprofile",
        null=True,)
    headline = models.CharField(blank=True, max_length=140)
    first_name = models.CharField(blank=True, max_length=140)
    last_name = models.CharField(blank=True, max_length=140)
    pheadline = models.CharField(blank=True, max_length=140)
    current_position = models.CharField(blank=True, max_length=140)
    education = models.CharField(blank=True, max_length=140)
    country_region = models.CharField(blank=True, max_length=140)
    location = models.CharField(blank=True, max_length=140)
    industry = models.CharField(blank=True, max_length=140)
    contact_information = models.CharField(blank=True, max_length=140)
    description = models.CharField(blank=True, max_length=140)
    school_name = models.CharField(blank=True, max_length=140)
    school_degree = models.CharField(blank=True, max_length=140)
    field_of_study = models.CharField(blank=True, max_length=140)
    location_of_school = models.CharField(blank=True, max_length=140)
    start_school = models.CharField(blank=True, max_length=140)
    end_school = models.CharField(blank=True, max_length=140)
    experience_title = models.CharField(blank=True, max_length=140)
    company_name = models.CharField(blank=True, max_length=140)
    company_location = models.CharField(blank=True, max_length=140)
    start_company = models.CharField(blank=True, max_length=140)
    end_company = models.CharField(blank=True, max_length=140)
    area_of_expertise = models.CharField(blank=True, max_length=140)
    project_name = models.CharField(blank=True, max_length=140)
    start_project = models.CharField(blank=True, max_length=140)
    end_project = models.CharField(blank=True, max_length=140)
    project_creator = models.CharField(blank=True, max_length=140)
    associated_with = models.CharField(blank=True, max_length=140)
    project_url = models.CharField(blank=True, max_length=140)
    project_description = models.CharField(blank=True, max_length=140)
    accomplishment_title = models.CharField(blank=True, max_length=140)
    accomplishment_associated_with = models.CharField(blank=True, max_length=140)
    issuer = models.CharField(blank=True, max_length=140)
    issue_date = models.CharField(blank=True, max_length=140)
    accomplishment_description = models.CharField(blank=True, max_length=140)
    SKILLS = [
        ('JAVA', 'JAVA'),
        ('CPP', 'CPP'),
        ('C', 'C'),
        ('Python', 'Python'),
        ('jQuery', 'jQuery'),
        ('Javascript', 'Javascript')
    ]
    skill_info = MultiSelectField(blank=True,default='',choices=SKILLS,max_length=540)

    def _str_(self):
        return self.name