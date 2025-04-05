from jobspy import scrape_jobs

def scrape_linkedin_jobs(query, location):
    jobs = scrape_jobs(
        site_name="linkedin",
        search_term=query,
        location=location or "Pakistan",
        results_wanted=40,
        country_indeed='Pakistan',
        hours_old=120
    )
    return jobs.to_dict(orient='records')
