from db import SessionLocal
from schemas import JobCreate
import crud

DUMMY = [
    JobCreate(title="Backend Engineer", company="Acme", location="Remote",
              url="https://x.com/somejob", raw_text="Hiring Backend Engineer (Python, FastAPI). Remote.", tweet_id="x1"),
    JobCreate(title="SDE Intern", company="BetaCorp", location="Bangalore",
              url="https://x.com/somejob2", raw_text="SDE Intern – Bangalore. Stipend 25k.", tweet_id="x2"),
]

if __name__ == "__main__":
    db = SessionLocal()
    for j in DUMMY:
        try:
            crud.create_job(db, j)
            print("Inserted:", j.title)
        except Exception as e:
            print("Skip/Err:", e)
    db.close()
