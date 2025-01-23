from django import forms

from .models import (
    CV,
    CVHeaderInfo,
    CVJobDescription,
    CVEducation,
    CVProject,
    CVLanguage,
    CVCertification,
    CVHardSkill,
    JobRecruitmentDescription,
)


date_input_widget = forms.DateInput(attrs={"type": "date"})


class CVNameForm(forms.ModelForm):
    class Meta:
        model = CV
        fields = ["full_name"]


class CVHeaderInfoForm(forms.ModelForm):
    class Meta:
        model = CVHeaderInfo
        fields = ["header_info"]


class CVJobDescriptionForm(forms.ModelForm):
    class Meta:
        model = CVJobDescription
        fields = [
            "job_description",
            "job_title",
            "company_name",
            "start_date",
            "end_date",
        ]

    start_date = forms.DateField(widget=date_input_widget)
    end_date = forms.DateField(widget=date_input_widget)


class EducationForm(forms.ModelForm):
    class Meta:
        model = CVEducation
        fields = [
            "school_name",
            "faculty",
            "degree",
            "start_date",
            "end_date",
            "details",
        ]

    start_date = forms.DateField(widget=date_input_widget)
    end_date = forms.DateField(widget=date_input_widget)


class ProjectForm(forms.ModelForm):
    class Meta:
        model = CVProject
        fields = ["project_name", "project_description"]


class LanguageForm(forms.ModelForm):
    class Meta:
        model = CVLanguage
        fields = ["language"]


class CertificationForm(forms.ModelForm):
    class Meta:
        model = CVCertification
        fields = ["certification"]


class HardSkillForm(forms.ModelForm):
    class Meta:
        model = CVHardSkill
        fields = ["hard_skill"]


class JobRecruitmentDescription(forms.ModelForm):
    class Meta:
        model = JobRecruitmentDescription
        fields = ["description"]


from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model


class EmailAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(widget=forms.EmailInput(attrs={"autofocus": True}))

    def confirm_login_allowed(self, user):
        if not user.is_active:
            raise forms.ValidationError("This account is inactive.", code="inactive")


User = get_user_model()


class RegistrationForm(forms.ModelForm):
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput,
        strip=False,
    )
    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput,
        strip=False,
    )

    class Meta:
        model = User
        fields = (
            "email",
            "first_name",
            "last_name",
        )  # Include fields you want users to fill

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
