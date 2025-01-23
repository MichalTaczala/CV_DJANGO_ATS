from django import forms

from .models import CV, CVHeaderInfo, CVJobDescription, CVEducation, CVProject, CVLanguage, CVCertification, CVHardSkill, JobRecruitmentDescription


date_input_widget = forms.DateInput(attrs={'type': 'date'})

class CVNameForm(forms.ModelForm):
    class Meta:
        model = CV
        fields = ['full_name']

class CVHeaderInfoForm(forms.ModelForm):
    class Meta:
        model = CVHeaderInfo
        fields = ['header_info']

class CVJobDescriptionForm(forms.ModelForm):
    class Meta:
        model = CVJobDescription
        fields = ['job_description', 'job_title', 'company_name', 'start_date', 'end_date']
    start_date = forms.DateField(widget=date_input_widget)
    end_date = forms.DateField(widget=date_input_widget)

class EducationForm(forms.ModelForm):
    class Meta:
        model = CVEducation
        fields = ['school_name', 'faculty', 'degree', 'start_date', 'end_date', 'details']
    start_date = forms.DateField(widget=date_input_widget)
    end_date = forms.DateField(widget=date_input_widget)


class ProjectForm(forms.ModelForm):
    class Meta:
        model = CVProject
        fields = ['project_name', 'project_description']

class LanguageForm(forms.ModelForm):
    class Meta:
        model = CVLanguage
        fields = ['language']

class CertificationForm(forms.ModelForm):
    class Meta:
        model = CVCertification
        fields = ['certification']

class HardSkillForm(forms.ModelForm):
    class Meta:
        model = CVHardSkill
        fields = ['hard_skill']

class JobRecruitmentDescription(forms.ModelForm):
    class Meta:
        model = JobRecruitmentDescription
        fields = ['description']