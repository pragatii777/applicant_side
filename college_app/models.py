from django.db import models
from django.core.validators import MaxLengthValidator, MinLengthValidator
from django.urls import reverse
from multiselectfield import MultiSelectField

# Create your models here.
from accounts.models import ProfcessUser
User = ProfcessUser
class CollegeUserProfile(models.Model):
    name = models.CharField(blank=True, max_length=140)
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        limit_choices_to={"usertype": "College"},
        related_name="collegeuserprofile"
    )
    location = models.CharField(blank=True, max_length=140)
    #cell = models.CharField('Contact Phone', blank=True, max_length=10,
                               #validators=[MaxLengthValidator(10), MinLengthValidator(10)])
    #HR_email = models.EmailField('Email Address', blank=True)
    designation=models.CharField(default='',blank=True, max_length=140)
    college_name=models.CharField(default='',blank=True, max_length=140)
    url_of_college=models.CharField(default='',blank=True, max_length=140)
    why_join_us=models.CharField(default='',blank=True, max_length=540)
    college_description=models.CharField(blank=True, max_length=540)

    def __str__(self):
        return self.name
    pass
class Job(models.Model):
    job_title = models.CharField(blank=True, max_length=140)
    posted_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        limit_choices_to={"usertype": "College"},
        related_name="college_jobs",
        default="def",
        blank=True)
    applied_by = models.ManyToManyField(
        User,
        related_name="applied_by_students",
        limit_choices_to={"usertype": "Applicant"},
        blank=True)
    company_name = models.CharField('company name', max_length=30, blank=True)

    job_salary = models.CharField('MONTHLY HAND IN SALARY', blank=True, max_length=140)
    job_vacancies = models.IntegerField('NO. OF OPENINGS', default=1, blank=True)
    TYPE_OF_JOB_CHOICES = [
        ('full time', 'FULL TIME'),
        ('contract', 'CONTRACT'),
        ('part time', 'PART TIME'),
        ('internship', 'INTERNSHIP'),
        ('volunteer', 'VOLUNTEER'),
        ('temporary', 'TEMPORARY'),
        ('remote', 'REMOTE'),
    ]
    type_of_job = models.CharField('TYPE OF JOB',
                                   max_length=35,
                                   choices=TYPE_OF_JOB_CHOICES,
                                   default=""
                                   )
    JOB_LOCATION_CHOICES = [
        ('wfh', 'Work From Home'),
        ('ahemdabad', 'Ahmedabad'),
        ('bengaluru', 'Bengaluru'),
        ('chennai', 'Chennai'),
        ('delhi', 'Delhi'),
        ('hydradad', 'Hyderabad'),
        ('jaipur', 'Jaipur'),
        ('kolkata', 'Kolkata'),
        ('mumbai', 'Mumbai'),
        ('pune', 'Pune'),
        ('surat', 'Surat'),
        ('vishakhapatnam', 'Vishakhapatnam')
    ]
    job_location = models.CharField('JOB LOCATION',
                                    max_length=35,
                                    choices=JOB_LOCATION_CHOICES,
                                    default=""
                                    )
    SKILLS = (
        ('JAVA', 'JAVA'),
        ('CPP', 'CPP'),
        ('C', 'C'),
        ('Python', 'Python'),
        ('jQuery', 'jQuery'),
        ('Javascript', 'Javascript')
    )
    job_requirements = MultiSelectField(choices=SKILLS,
                                        blank=True,
                                        max_length=540)
    job_info = models.CharField(blank=True,
                                max_length=540)
    date = models.DateTimeField('Expected Hiring Date', auto_now_add=False, auto_now=False, blank=True, null=True)
    work_choice = models.CharField('Does this job allow hires to work remote?', max_length=100, default="",
                                   choices=[('Yes', 'Yes'),
                                            ('No', 'No'),
                                            ('Temporary due to COVID-19', 'Temporary due to COVID-19')
                                            ])
    # job_starting_date = models.DateTimeField(
    #     verbose_name=_('Date joined'), auto_now_add=True)

    def __str__(self):
        return self.job_title
    pass

    def  get_absolute_url(self):    # redirect to job details after updation
        return reverse('college:job_detail' , kwargs={'pk': self.pk})
