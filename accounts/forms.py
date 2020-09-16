from django import forms
from .models import ProfcessUser
from django.core.exceptions import ValidationError
from django.contrib.auth import (
    authenticate, get_user_model, password_validation,
)
from django.utils.translation import gettext, gettext_lazy as _
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget

class UserCreationForm(forms.ModelForm):
    """
    A form that creates a user, with no privileges, from the given username email and
    password.
    """
    error_messages = {
        'password_mismatch': _('The two password fields didn’t match.'),
        'strong_password': _('Enter strong password.Your password must contain a Alphabet and a number'),
    }
    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label=_("Confirm Pass"),
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        strip=False,
        help_text=_("Enter the same password as before, for verification."),
    )
    phone=PhoneNumberField(widget=PhoneNumberPrefixWidget(initial='IN'))

    class Meta:
        model = ProfcessUser
        fields = ("username", "email",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self._meta.model.USERNAME_FIELD in self.fields:
            self.fields[self._meta.model.USERNAME_FIELD].widget.attrs['autofocus'] = True

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2
    def clean_password1(self):
        password1 = self.cleaned_data.get("password1")
        first_isalpha=password1[0].isalpha()
        if all(c.isalpha()==first_isalpha or c=='@' or c=='#' for c in password1):
            raise ValidationError(
                self.error_messages['strong_password'],
                code='strong_password',
            )

        return password1

    

    def _post_clean(self):
        super()._post_clean()
        # Validate the password after self.instance is updated with form data
        # by super().
        password = self.cleaned_data.get('password2')
        if password:
            try:
                password_validation.validate_password(password, self.instance)
            except ValidationError as error:
                self.add_error('password2', error)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class RecruiterCreationForm(forms.ModelForm):
    """
    A form that creates a user with usertyper equals Recruiter, with no privileges, from the given username email and
    password.
    """
    error_messages = {
        'password_mismatch': _('The two password fields didn’t match.'),
        'strong_password': _('Enter strong password.Your password must contain a Alphabet a Number'),
    }
    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
    )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        strip=False,
        help_text=_("Enter the same password as before, for verification."),
    )

    class Meta:
        model = ProfcessUser
        fields = ("username", "email", "first_name", "last_name", "phone", "company_name","designation","location","url_of_company","why_join_us","company_description",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self._meta.model.USERNAME_FIELD in self.fields:
            self.fields[self._meta.model.USERNAME_FIELD].widget.attrs['autofocus'] = True

    ''' clean_phoneNumber(self):
        phone_number = self.cleaned_data['phone']
        print(phone_number)
        # Replace 'US' with whatever type of number it is
        # See https://github.com/daviddrysdale/python-phonenumbers
        parsed_number = phonenumbers.parse(phone_number, 'IN')
        print(phone_number)
        print(parsed_number)
        return phonenumbers.format_number(
            parsed_number,
            phonenumbers.PhoneNumberFormat.E164,
        )
'''
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2
    def clean_password1(self):
        password1 = self.cleaned_data.get("password1")
        first_isalpha=password1[0].isalpha()
        if all(c.isalpha()==first_isalpha or c=='@' or c=='#' or c=='!' or c=='$' or c=='%' or c=='^' or c=='~' or c=='&' or c=='*'
         for c in password1):
            raise ValidationError(
                self.error_messages['strong_password'],
                code='strong_password',
            )
        return password1

    def _post_clean(self):
        super()._post_clean()
        # Validate the password after self.instance is updated with form data
        # by super().
        password = self.cleaned_data.get('password2')
        if password:
            try:
                password_validation.validate_password(password, self.instance)
            except ValidationError as error:
                self.add_error('password2', error)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.usertype = "Recruiter"
        if commit:
            user.save()
        return user


class ApplicantCreationForm(forms.ModelForm):
    """
    A form that creates a user with usertype equals Applicant, with no privileges, from the given username email and
    password.
    """
    error_messages = {
        'password_mismatch': _('The two password fields didn’t match.'),
        'strong_password': _('Enter strong password.Your password must contain a Alphabet and a number'),
    }
    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        strip=False,
        help_text=_("Enter the same password as before, for verification."),
    )

    class Meta:
        model = ProfcessUser
        fields = ("username", "email","first_name","last_name", "email","phone")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self._meta.model.USERNAME_FIELD in self.fields:
            self.fields[self._meta.model.USERNAME_FIELD].widget.attrs['autofocus'] = True

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2
    def clean_password1(self):
        password1 = self.cleaned_data.get("password1")
        first_isalpha=password1[0].isalpha()
        if all(c.isalpha()==first_isalpha for c in password1):
            raise ValidationError(
                self.error_messages['strong_password'],
                code='strong_password',
            )
        return password1

    def _post_clean(self):
        super()._post_clean()
        # Validate the password after self.instance is updated with form data
        # by super().
        password = self.cleaned_data.get('password2')
        if password:
            try:
                password_validation.validate_password(password, self.instance)
            except ValidationError as error:
                self.add_error('password2', error)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.usertype = "Applicant"
        if commit:
            user.save()
        return user

class CollegeCreationForm(forms.ModelForm):
    """
    A form that creates a user with usertyper equals Recruiter, with no privileges, from the given username email and
    password.
    """
    error_messages = {
        'password_mismatch': _('The two password fields didn’t match.'),
        'strong_password': _('Enter strong password.Your password must contain a Alphabet and a number'),
    }
    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
    )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        strip=False,
        help_text=_("Enter the same password as before, for verification."),
    )

    class Meta:
        model = ProfcessUser
        fields = ("username", "email", "first_name", "last_name", "phone", "college_name","designation","location","url_of_college","why_join_us","college_description",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self._meta.model.USERNAME_FIELD in self.fields:
            self.fields[self._meta.model.USERNAME_FIELD].widget.attrs['autofocus'] = True

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2
    def clean_password1(self):
        password1 = self.cleaned_data.get("password1")
        first_isalpha=password1[0].isalpha()
        if all(c.isalpha()==first_isalpha for c in password1):
            raise ValidationError(
                self.error_messages['strong_password'],
                code='strong_password',
            )
        return password1

    def _post_clean(self):
        super()._post_clean()
        # Validate the password after self.instance is updated with form data
        # by super().
        password = self.cleaned_data.get('password2')
        if password:
            try:
                password_validation.validate_password(password, self.instance)
            except ValidationError as error:
                self.add_error('password2', error)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.usertype = "College"
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField(
        label=_("Password"),
        help_text=_(
            'Raw passwords are not stored, so there is no way to see this '
            'user’s password, but you can change the password using '
            '<a href="{}">this form</a>.'
        ),
    )

    class Meta:
        model = ProfcessUser
        fields = '__all__'

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     password = self.fields.get('password')
    #     if password:
    #         password.help_text = password.help_text.format('../password/')
    #     user_permissions = self.fields.get('user_permissions')
    #     if user_permissions:
    #         user_permissions.queryset = user_permissions.queryset.select_related('content_type')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]

class EmailForm(forms.ModelForm):
    class Meta:
        model = ProfcessUser
        fields = ('verified_email',)

