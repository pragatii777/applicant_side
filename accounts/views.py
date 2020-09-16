
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.urls import reverse_lazy
from django.views.generic import CreateView, View
from .forms import RecruiterCreationForm, ApplicantCreationForm,CollegeCreationForm,EmailForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes,force_text,DjangoUnicodeDecodeError
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from .models import ProfcessUser
from django.contrib import messages
from django.http import HttpResponse
from django.core.mail import send_mail
from .token import activation_token
from applicant_app.models import ApplicantUserProfile
from recruiter_app.forms import UserProfileForm,UserUpdateForm
from django.core.exceptions import ObjectDoesNotExist
from applicant_app.forms import UserProfileForm,UserProfileUpdationForm
from college_app.forms import UserUpdateFormCollege,UserProfileForm,CollegeUserProfile


# Create your views here.
def index(request):
    p=ProfcessUser.objects.all()
    if request.user in p:
        if request.user.usertype=='Recruiter':
            if request.user.activated == False:
                messages.info(request, "You have not confirmed your email address yet."
                                       " If you cannot find your confirmation email anymore, send yourself a new one here.")
                set=True
            if request.method == 'POST':
                u_form = UserUpdateForm(request.POST, instance=request.user)
                if u_form.is_valid():
                    u_form.save()
                    return render(request,'recruiter_app/update_success.html')
            else:
                u_form = UserUpdateForm(instance=request.user)
            context = {
                'u_form': u_form,
            }
            return render(request, 'recruiter_app/profile.html', context)
        elif request.user.usertype=='Applicant':
            if request.user.activated == False:
                messages.info(request, "You have not confirmed your email address yet. "
                                       "If you cannot find your confirmation email anymore, send yourself a new one here.")
                set = True
            try:
                UserProfileUpdationForm(instance=request.user.applicantuserprofile)
            except ObjectDoesNotExist:
                return redirect("applicant:create_applicant_profile")
            form = UserProfileUpdationForm(instance=request.user.applicantuserprofile)
            args = {'form': form}
            return render(request, "applicant_app/userprofileform.html", args)
        elif request.user.usertype=='College':
            if request.user.activated == False:
                messages.info(request, "You have not confirmed your email address yet."
                                       " If you cannot find your confirmation email anymore, send yourself a new one here.")
                set = True
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

        else:
            return render(request, "index.html")
    else:
        return render(request, "index.html")
def about(request):
    return render(request, "about.html")
    pass

def contact(request):
    return render(request, "contact.html")
    pass

def findJob(request):
    return render(request, "findJob.html")
    pass
def careerAdvice(request):
    return render(request, "careerAdvice.html")
    pass
def findATalent(request):
    return render(request, "findATalent.html")
    pass
def services(request):
    return render(request, "services.html")
    pass
def recruiter_signup(request):
        form = RecruiterCreationForm(request.POST or None)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            site = get_current_site(request)
            mail_subject = 'Confirmation message'
            message = render_to_string('registration/activate.html', {
                'user': user,
                'domain': site.domain,
                'uid': user.pk,
                'token': activation_token.make_token(user)
            })
            to_email = form.cleaned_data.get('email')
            to_list = [to_email]
            from_email = settings.EMAIL_HOST_USER
            send_mail(mail_subject, message, from_email, to_list, fail_silently=True)


            new_user = authenticate(username=form.cleaned_data['email'],
                                    password=form.cleaned_data['password1'],
                                    )
            login(request, new_user)
            return redirect('accounts:index')
        return render(request, 'registration/signup.html', {"form": form})
def activate(request,uid,token):
    request.user.activated=True
    request.user.save()
    return redirect('accounts:index')

def email_form(request):
        if request.method == "POST":
            eform = EmailForm(request.POST or None)
            if eform.is_valid():
                p = ProfcessUser.objects.get(pk=request.user.pk)
                user = eform.save(commit=False)
                site = get_current_site(request)
                mail_subject = 'Confirmation message'
                message = render_to_string('registration/activate.html', {
                    'user': user,
                    'domain': site.domain,
                    'uid': user.pk,
                    'token': activation_token.make_token(user)
                })
                to_email = eform.cleaned_data.get('verified_email')
                p.verified_email = to_email
                p.save()
                to_list = [to_email]
                from_email = settings.EMAIL_HOST_USER
                send_mail(mail_subject, message, from_email, to_list, fail_silently=True)
                user.verified_email = to_email
                return redirect('accounts:index')
                pass
            else:
                eform = EmailForm(request.POST or None)
                return render(request, 'registration/email_form.html', {"form": eform})
                pass
        else:
            eform = EmailForm(request.POST or None)
            return render(request, 'registration/email_form.html', {"form": eform})
            pass



def showprivacy(request):
    return render(request,'registration/privacy.html')
    
def showterms(request):
    return render(request,'registration/terms.html') 
    
def dashboard(request):
    return render(request,'dashboard.html')

def ApplicantSignUp(request):
        form = ApplicantCreationForm(request.POST or None)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            site = get_current_site(request)
            mail_subject = 'Confirmation message'
            message = render_to_string('registration/activate.html', {
                'user': user,
                'domain': site.domain,
                'uid': user.pk,
                'token': activation_token.make_token(user)
            })
            to_email = form.cleaned_data.get('email')
            to_list = [to_email]
            from_email = settings.EMAIL_HOST_USER
            send_mail(mail_subject, message, from_email, to_list, fail_silently=True)

            new_user = authenticate(username=form.cleaned_data['email'],
                                    password=form.cleaned_data['password1'],
                                    )
            login(request, new_user)
            return redirect('accounts:index')
        return render(request, 'registration/signup.html', {"form": form})

def college_signup(request):
    form = CollegeCreationForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        user.save()
        site = get_current_site(request)
        mail_subject = 'Confirmation message'
        message = render_to_string('registration/activate.html', {
            'user': user,
            'domain': site.domain,
            'uid': user.pk,
            'token': activation_token.make_token(user)
        })
        to_email = form.cleaned_data.get('email')
        to_list = [to_email]
        from_email = settings.EMAIL_HOST_USER
        send_mail(mail_subject, message, from_email, to_list, fail_silently=True)

        new_user = authenticate(username=form.cleaned_data['email'],
                                password=form.cleaned_data['password1'],
                                )
        login(request, new_user)
        return redirect('accounts:index')
    return render(request, 'registration/signup.html', {"form": form})

def get_context(request):
    if (request.user.is_authenticated):
        context=ApplicantUserProfile.objects.filter(user=request.user).values()[0]
        #conversion=model_to_dict(reqfield)
        context.pop('id')
        context.pop('user_id')
        return context








