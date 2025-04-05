
import requests

HF_API_TOKEN = "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"
API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-mnli"

headers = {
    "Authorization": f"Bearer {HF_API_TOKEN}"
}

def query_zero_shot(premise: str, label: str):
    payload = {
        "inputs": premise,
        "parameters": {
            "candidate_labels": [label],
            "multi_label": False
        }
    }

    response = requests.post(API_URL, headers=headers, json=payload)
    response.raise_for_status()
    return response.json()

def filter_relevant_jobs(jobs, user_input: str, top_k: int = 10):
    if not jobs:
        return []

    scored_jobs = []

    for job in jobs:
        # Combine various job fields to better represent the job for relevance comparison
        combined_text = " ".join([
            str(job.get("title", "")),
            str(job.get("location", "")),
            str(job.get("description", "")),
            str(job.get("salary", "")),
            str(job.get("employment_type", "")),
            str(job.get("experience_level", "")),
            str(job.get("skills", ""))  # assuming there's a field like this
        ])

        if not combined_text.strip():
            continue

        try:
            result = query_zero_shot(combined_text, user_input)
            score = result["scores"][0]  # Relevance score for the label
            job["relevance_score"] = round(score, 2)
            scored_jobs.append(job)
        except Exception as e:
            print(f"Error processing job: {e}")

    # Sort jobs by descending relevance
    scored_jobs.sort(key=lambda x: x["relevance_score"], reverse=True)
    return scored_jobs[:top_k]