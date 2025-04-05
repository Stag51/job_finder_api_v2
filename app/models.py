from pydantic import BaseModel

class JobSearchRequest(BaseModel):
    position: str
    experience: str | None = None
    salary: str | None = None
    jobNature: str | None = None  # Changed from jobNature to job_nature
    location: str
    skills: str | None = None

