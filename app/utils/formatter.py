def format_jobs(jobs):
    return [
        {
            "job_title": job.get("title"),
            "company": job.get("company"),
            "experience": job.get("experience"),
            "location": job.get("location"),
            "salary": job.get("salary"),
            "url": job.get("job_url"),
            "jobNature":job.get("jobNature"),
        }
        for job in jobs
    ]
