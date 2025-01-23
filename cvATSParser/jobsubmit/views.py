import os
from django.forms import modelformset_factory
from django.http import FileResponse, JsonResponse
from django.shortcuts import redirect, render
import json
from django.views import View

from .open_ai_service import OpenAIService

from .models import (
    CVHeaderInfo,
    CVJobDescription,
    CVEducation,
    CVProject,
    CVLanguage,
    CVCertification,
    CVHardSkill,
    CV,
)

from .forms import (
    CVNameForm,
    CVHeaderInfoForm,
    CVJobDescriptionForm,
    EducationForm,
    ProjectForm,
    LanguageForm,
    CertificationForm,
    HardSkillForm,
    JobRecruitmentDescription,
)

from .services import (
    transform_job_description,
    transform_education_record,
    render_latex,
)
from .pdf_service import generate_pdf_from_latex


FORMSET_DEFINITIONS = [
    (CVHeaderInfo, CVHeaderInfoForm, "header"),
    (CVJobDescription, CVJobDescriptionForm, "experience"),
    (CVEducation, EducationForm, "education"),
    (CVProject, ProjectForm, "project"),
    (CVLanguage, LanguageForm, "language"),
    (CVCertification, CertificationForm, "certification"),
    (CVHardSkill, HardSkillForm, "hard_skill"),
]


# Utility function to create formsets dynamically
def create_formsets(extra=1, add_prefix=False):
    if add_prefix:
        return {
            prefix: modelformset_factory(model, form=form, extra=extra)(prefix=prefix)
            for model, form, prefix in FORMSET_DEFINITIONS
        }
    return {
        prefix: modelformset_factory(model, form=form, extra=extra)
        for model, form, prefix in FORMSET_DEFINITIONS
    }


class CVCreateView(View):
    def get(self, request):
        formsets = create_formsets(add_prefix=True)
        context = self.build_context(formsets)
        return render(request, "jobsubmit/cv_create.html", context)

    def post(self, request):
        formsets = create_formsets()
        cv_form = CVNameForm(request.POST)
        formsets_instances = self.initialize_formsets(formsets, request.POST)

        if self.validate_formsets(cv_form, formsets_instances):
            _ = self.save_cv_data(cv_form, formsets_instances)
            return redirect("/addJobDescription")

        context = self.build_context(formsets_instances, cv_form)
        return render(request, "jobsubmit/cv_create.html", context)

    def build_context(self, formsets, cv_form=None):
        context = {"form_name": cv_form or CVNameForm()}
        context.update(
            {f"formset_{prefix}": formset for prefix, formset in formsets.items()}
        )
        return context

    def save_cv_data(self, cv_form, formsets_instances):
        """Save CV and associated data."""
        cv = CV.objects.create(full_name=cv_form.cleaned_data["full_name"])
        cv_data = {
            "header_info": [
                form.cleaned_data["header_info"]
                for form in formsets_instances["header"]
            ],
            "work_experience": [
                {
                    **form.cleaned_data,
                    "start_date": (
                        form.cleaned_data["start_date"].strftime("%Y-%m-%d")
                        if form.cleaned_data["start_date"]
                        else None
                    ),
                    "end_date": (
                        form.cleaned_data["end_date"].strftime("%Y-%m-%d")
                        if form.cleaned_data["end_date"]
                        else None
                    ),
                }
                for form in formsets_instances["experience"]
            ],
            "education": [
                {
                    **form.cleaned_data,
                    "start_date": (
                        form.cleaned_data["start_date"].strftime("%Y-%m-%d")
                        if form.cleaned_data["start_date"]
                        else None
                    ),
                    "end_date": (
                        form.cleaned_data["end_date"].strftime("%Y-%m-%d")
                        if form.cleaned_data["end_date"]
                        else None
                    ),
                }
                for form in formsets_instances["education"]
            ],
            "projects": [form.cleaned_data for form in formsets_instances["project"]],
            "languages": [
                form.cleaned_data["language"] for form in formsets_instances["language"]
            ],
            "certifications": [
                form.cleaned_data["certification"]
                for form in formsets_instances["certification"]
            ],
            "hard_skills": [
                form.cleaned_data["hard_skill"]
                for form in formsets_instances["hard_skill"]
            ],
        }
        cv.data = cv_data
        cv.save()
        return cv

    def initialize_formsets(self, formsets, data):
        return {
            prefix: formset(data, prefix=prefix)
            for (_, _, prefix), formset in zip(FORMSET_DEFINITIONS, formsets.values())
        }

    def validate_formsets(self, cv_form, formsets_instances):
        validities = [
            cv_form.is_valid(),
            *[formset.is_valid() for formset in formsets_instances.values()],
        ]

        return all(validities)


class AddJobDescView(View):
    def get(self, request):
        return render(
            request,
            "jobsubmit/add_job_description.html",
            {
                "job_desc_form": JobRecruitmentDescription(),
                "name_form": CVNameForm(),
            },
        )

    def post(self, request):
        """Handle POST request to process job description."""
        job_desc_form = JobRecruitmentDescription(request.POST)
        name_form = CVNameForm(request.POST)

        if job_desc_form.is_valid() and name_form.is_valid():
            name_from_user = name_form.cleaned_data["full_name"]
            job_desc = job_desc_form.cleaned_data["description"]

            cv = CV.objects.filter(full_name=name_from_user).last()
            if not cv:
                return JsonResponse({"error": "CV not found."}, status=404)

            json_for_ai_api = self.build_open_ai_json(cv.data)
            response_json = self.submit_to_openai(job_desc, json_for_ai_api)
            cv.data = self.update_cv_data(cv.data, response_json)
            rendered_latex = render_latex(cv.data, self.get_template_file())
            output_pdf = generate_pdf_from_latex(rendered_latex)
            return FileResponse(
                open(output_pdf, "rb"),
                as_attachment=True,
                filename=f"{cv.full_name}.pdf",
            )

        return JsonResponse({"error": "Invalid form submission."}, status=400)

    def build_open_ai_json(self, cv_json):
        """Build JSON payload for OpenAI API."""
        return {
            "educations": transform_education_record(cv_json["education"]),
            "workExperience": transform_job_description(cv_json["work_experience"]),
            "projects": cv_json["projects"],
            "languages": cv_json["languages"],
            "certifications": cv_json["certifications"],
            "hard_skills_to_choose_from": cv_json["hard_skills"],
        }

    def submit_to_openai(self, job_desc, json_payload):
        """Submit data to OpenAI and return the response."""
        openai_service = OpenAIService()
        response = openai_service.submit_job(job_desc, json_payload)
        cleaned_response = response.content.replace("json", "").strip()
        return json.loads(cleaned_response)

    def update_cv_data(self, cv_json, response_json):
        cv_json["summary"] = response_json["summary"]
        cv_json["projects"] = response_json["the_most_related_projects_for_this_job"]
        cv_json["hard_skills"] = response_json["hard_skills"]
        cv_json["soft_skills"] = response_json["soft_skills"]

        for i, education in enumerate(cv_json["education"]):
            education.update(response_json["education"][i])

        for i, experience in enumerate(cv_json["work_experience"]):
            experience.update(response_json["experience"][i])

        return cv_json

    def get_template_file(self):
        template_file = os.path.join(
            os.path.dirname(__file__), "templates", "latex", "cv_template.tex"
        )
        if not os.path.exists(template_file):
            raise FileNotFoundError("Template file not found.")
        return template_file
