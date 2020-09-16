from django.contrib import admin
from .models import RecruiterUserProfile, Job,Short_list_candidate,UserData
# Register your models here.
admin.site.register(RecruiterUserProfile)
admin.site.register(Job)
admin.site.register(Short_list_candidate)
admin.site.register(UserData)