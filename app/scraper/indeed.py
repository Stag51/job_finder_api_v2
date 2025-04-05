from jobspy import scrape_jobs

def scrape_indeed_jobs(query, location):
    jobs = scrape_jobs(
        site_name="indeed",
        search_term=query,
        location=location or "Pakistan",
        results_wanted=40,
        country_indeed='Pakistan',
        hours_old=240
    )
    return jobs.to_dict(orient='records')
