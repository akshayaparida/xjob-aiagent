from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from db import Base, engine, SessionLocal
from schemas import JobOut, JobCreate, SubscribeIn, SubscribeOut
import crud

Base.metadata.create_all(bind=engine)

app = FastAPI(title="TweetHire Backend")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/", tags=["health"])
def health():
    return {"status": "ok"}

@app.get("/jobs", response_model=list[JobOut], tags=["jobs"])
def get_jobs(limit: int = 50, db: Session = Depends(get_db)):
    return crud.list_jobs(db, limit=limit)

@app.post("/jobs", response_model=JobOut, tags=["jobs"])
def create_job(payload: JobCreate, db: Session = Depends(get_db)):
    try:
        return crud.create_job(db, payload)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/subscribe", response_model=SubscribeOut, tags=["subs"])
def subscribe(body: SubscribeIn, db: Session = Depends(get_db)):
    try:
        return crud.add_subscriber(db, body)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
