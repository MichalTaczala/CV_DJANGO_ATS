from django.http import HttpResponse
from django.template.loader import get_template


def debug_template_view(request):
    try:
        template = get_template('jobsubmit/job_submit_form.html')
        return HttpResponse("Template found!")
    except Exception as e:
        return HttpResponse(f"Template error: {e}")
def homepage(request):
    return HttpResponse("Hello, World!")
def about(request):
    return HttpResponse("About me")