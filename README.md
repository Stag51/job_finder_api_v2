# 🔍 Job Finder API

 A FastAPI-based intelligent job scraping and matching API that aggregates listings from LinkedIn, Indeed, and one additional job portal. 
 It processes job search criteria using LLMs to return only the most relevant listings, structured and ready for consumption.

 ---

 ## 📌 Overview

 This project serves as a **Machine Learning Engineer Assessment** and demonstrates your ability to:

 - Build robust APIs with FastAPI.
 - Integrate web scraping tools (BeautifulSoup/Selenium/Scrapy).
 - Fetch jobs from online platforms: **LinkedIn**, **Indeed**, and a third source **Google Jobs**
 - Use **LLMs (OpenAI/HuggingFace)** to analyze and rank job descriptions based on user-defined relevance.

 ---

 ## ⚙️ Tech Stack

 - **FastAPI** – API framework  
 - **Python** – Core language  
 - **BeautifulSoup / Selenium** – Web scraping  
 - **HTTPX / Requests** – Making API calls  
 - **OpenAI / HuggingFace Transformers / LangChain** – Relevance scoring with LLMs  
 - **Pydantic** – Input/output data models  

 ---

 ## 🧩 Architecture & Workflow

 ```plaintext
 User Input (JSON) ──▶ FastAPI Endpoint
                          │
                          ▼
         Fetch jobs from LinkedIn, Indeed, Google Jobs (Scrapers)
                          │
                          ▼
        Match relevance using LLMs (HuggingFace)
                          │
                          ▼
          Return structured JSON with relevant jobs
 ```

 ---

 ## 📥 API Endpoint

 ### `POST /search_jobs`

 **Request Body (JSON):**
 ```json
 {
   "position": "Full Stack Engineer",
   "experience": "2 years",
   "salary": "70,000 PKR to 120,000 PKR",
   "jobNature": "onsite",
   "location": "Peshawar, Pakistan",
   "skills": "full stack, MERN"
 }
 ```

 **Response Format:**
 ```json
 [
   {
     "title": "Full Stack Developer",
     "company": "Tech Innovations",
     "location": "Peshawar, Pakistan",
     "summary": "Looking for a MERN full stack developer with 2+ years experience...",
     "apply_link": "https://...",
     "source": "LinkedIn"
   },
   ...
 ]
 ```

 ---

 ## 📁 Project Structure

 ```
 job_finder_api/
 ├── app/
 │   ├── scraper/           # Scrapers for LinkedIn, Indeed, Rozee.pk
 │   ├── services/          # LLM relevance logic and utilities
 │   ├── utils/             # Helper functions
 │   ├── main.py            # FastAPI entrypoint
 │   ├── config.py          # Configuration (API keys, etc.)
 │   ├── models.py          # Request/response models
 ├── example_data.txt       # Sample input/output
 ├── requirements.txt       # Python dependencies
 ```

 ---

 ## 🚀 Getting Started

 ### 1. Clone the Repository
 ```bash
 git clone https://github.com/yourusername/job_finder_api.git
 cd job_finder_api
 ```

 ### 2. Install Dependencies
 ```bash
 pip install -r requirements.txt
 ```

 ### 3. Run the API
 ```bash
 uvicorn app.main:app --reload
 ```

 The API will be available at `http://127.0.0.1:8000`

 ---

 ## 💡 LLM Integration

 - Supports OpenAI GPT or HuggingFace transformers  
 - Relevant job descriptions are selected based on semantic similarity to user criteria  

 ---

 ## 🧪 Sample Testing

 Use a REST client like Postman or `curl`:
 ```bash
 curl -X POST http://127.0.0.1:8000/search_jobs \
      -H "Content-Type: application/json" \
      -d '{
            "position": "Full Stack Engineer",
            "experience": "2 years",
            "salary": "70,000 PKR to 120,000 PKR",
            "jobNature": "onsite",
            "location": "Peshawar, Pakistan",
            "skills": "full stack, MERN"
          }'
 ```

 ---

 ## 📌 Notes

 - It may give the output with null values because some job descriptions doesn't provide every thing like salary etc.  
   
 
 ---
 ## 👨‍💻 Author

 **Your Name**  
 [LinkedIn]([https://linkedin.com/in/yourprofile](https://www.linkedin.com/in/saad51)) | [GitHub](https://github.com/Stag51)
