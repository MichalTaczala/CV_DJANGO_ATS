import os
from dotenv import load_dotenv
from pydantic import BaseModel
from openai import OpenAI


class ExperienceTemplate(BaseModel):
    job_name: str
    details: list[str]


class EducationTemplate(BaseModel):
    degree: str
    details: list[str]


class ProjectTemplate(BaseModel):
    project_name: str
    details: list[str]


class CVOutputApi(BaseModel):
    summary: str
    experience: list[ExperienceTemplate]
    education: list[EducationTemplate]
    the_most_related_projects_for_this_job: list[ProjectTemplate]
    soft_skills: list[str]
    hard_skills: list[str]


class OpenAIService:
    def __init__(self, model_name="gpt-4o-mini"):
        load_dotenv()
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("API key for OpenAI is not set")
        self.client = OpenAI(api_key=api_key)
        self.model_name = model_name

    def submit_job(self, job_description, current_user_data):
        try:

            completion = self.client.beta.chat.completions.parse(
                model=self.model_name,
                store=True,
                response_format=CVOutputApi,
                messages=[
                    {
                        "role": "user",
                        "content": f"""I will give you json with information about me, and a job description.  Your goal is to rephrase the data in a way so json created out of it can pass ATS for this job. Try to include key words for this exact job. Add as many soft skills as needed, but don't add the hard skills that I haven't mentioned in the information about me. I don't know frontend at all so don't mention that. The job description is as follows {str(job_description)}, and the data is as follows:{str(current_user_data)}""",
                    },
                ],
            )
            return completion.choices[0].message
        except Exception as e:
            raise RuntimeError(f"Error while submitting job to OpenAI: {str(e)}")
