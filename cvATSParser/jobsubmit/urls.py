from django.urls import path
from .views import CVCreateView, AddJobDescView
from .views import EmailLoginView, CustomLogoutView, RegistrationView, dashboard

urlpatterns = [
    path("createCV/", CVCreateView.as_view(), name="create_cv"),
    path("addJobDescription/", AddJobDescView.as_view(), name="add_job_description"),
    path("login/", EmailLoginView.as_view(), name="login"),
    path("logout/", CustomLogoutView.as_view(), name="logout"),
    path("register/", RegistrationView.as_view(), name="register"),
    path("dashboard/", dashboard, name="dashboard"),
]
