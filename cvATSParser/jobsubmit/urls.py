from django.urls import path
from .views import CVCreateView, AddJobDescView

urlpatterns = [
    path("createCV", CVCreateView.as_view(), name="job_submit"),
    path("addJobDescription", AddJobDescView.as_view(), name="add_job_description"),
]
