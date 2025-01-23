from jinja2 import Environment, FileSystemLoader
import os
import json
from datetime import datetime
from .open_ai_service import OpenAIService


def transform_job_description(job_json_list):
    res = []
    for job_json in job_json_list:
        start_date = datetime.strptime(job_json["start_date"], "%Y-%m-%d")
        end_date = datetime.strptime(job_json["end_date"], "%Y-%m-%d")
        duration_in_months = (end_date.year - start_date.year) * 12 + (
            end_date.month - start_date.month
        )
        duration = f"{duration_in_months} months"
        res.append(
            {
                "how_long": duration,
                "details": job_json["job_description"],
            }
        )
    return res


def transform_education_record(education_json_list):
    res = []
    for education_json in education_json_list:
        res.append(
            {
                "degree": education_json["degree"],
                "start_date": education_json["start_date"],
                "end_date": education_json["end_date"],
                "details": education_json["details"],
            }
        )
    return res


def generate_cv_json(cv_data, job_description):
    openai_service = OpenAIService()
    response = openai_service.submit_job(job_description, cv_data)
    response_json = json.loads(response.content.replace("json", "").strip())
    return response_json


def render_latex(cv_json, template_file):
    env = Environment(
        block_start_string="[%",
        block_end_string="%]",
        variable_start_string="[[",
        variable_end_string="]]",
        comment_start_string="[COMMENT#",
        comment_end_string="#]",
        loader=FileSystemLoader(os.path.dirname(template_file)),
    )
    template = env.get_template(os.path.basename(template_file))
    return template.render(cv_json)
