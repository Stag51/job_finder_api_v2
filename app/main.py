
from fastapi import FastAPI, BackgroundTasks
from app.models import JobSearchRequest
from app.services.job_fetcher import fetch_all_jobs
from app.services.relevance_filter import filter_relevant_jobs
from app.utils.formatter import format_jobs


app = FastAPI()

@app.post("/search_jobs")
def search_jobs(request: JobSearchRequest):
    user_query = f"{request.position} {request.experience or ''} {request.skills or ''} {request.location or ''} {request.salary or ''} "

    all_jobs = fetch_all_jobs(
        position=request.position,
        location=request.location
    )

    # Use the Hugging Face LLM-based filter
    filtered_jobs = filter_relevant_jobs(all_jobs, user_query)

    return {"results": format_jobs(filtered_jobs)}