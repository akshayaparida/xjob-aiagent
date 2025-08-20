from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Job AI Agent Backend is running 🚀"}

@app.get("/jobs")
def get_jobs():
    # Placeholder: later connect to Portia agent / Twitter scraper
    return {"jobs": ["Software Engineer - Remote", "Backend Developer - Bangalore"]}

@app.post("/subscribe")
def subscribe(email: str, keywords: str):
    # TODO: Save to Postgres
    return {"status": "subscribed", "email": email, "keywords": keywords}
