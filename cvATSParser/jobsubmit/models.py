from django.db import models
from django.utils import timezone


class CV(models.Model):
    full_name = models.CharField(max_length=255, default="")
    created_at = models.DateTimeField(default=timezone.now)
    data = models.JSONField(default=dict)


class CVHeaderInfo(models.Model):
    header_info = models.CharField(max_length=255)


class CVJobDescription(models.Model):
    job_title = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    job_description = models.TextField()


class CVEducation(models.Model):
    school_name = models.CharField(max_length=255)
    faculty = models.CharField(max_length=255)
    degree = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    details = models.TextField()


class CVProject(models.Model):
    project_name = models.CharField(max_length=255)
    project_description = models.TextField()


class CVLanguage(models.Model):
    language = models.CharField(max_length=255)


class CVCertification(models.Model):
    certification = models.CharField(max_length=255)


class CVHardSkill(models.Model):
    hard_skill = models.CharField(max_length=255)


class JobRecruitmentDescription(models.Model):
    description = models.TextField()
