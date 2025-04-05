
from app.scraper.linkedin import scrape_linkedin_jobs
from app.scraper.indeed import scrape_indeed_jobs
from app.scraper.google import scrape_google_jobs


def fetch_all_jobs(position: str, location: str):
    
    linkedin_jobs = scrape_linkedin_jobs(position, location)  # Pass position and location
    indeed_jobs = scrape_indeed_jobs(position, location)      # Pass position and location
    google_jobs = scrape_google_jobs(position, location)  # Uncomment if Rozee is included

    # Combine all job listings
    all_jobs =  indeed_jobs + linkedin_jobs + google_jobs  
    return all_jobs
