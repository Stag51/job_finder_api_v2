from jobspy import scrape_jobs

def scrape_google_jobs(query, location):
    jobs = scrape_jobs(
        site_name="google",
        search_term=query,
        location=location or "Pakistan",
        results_wanted=20,
        country_indeed='Pakistan',
        hours_old=240
    )
    return jobs.to_dict(orient='records')
