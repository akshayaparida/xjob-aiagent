from sqlalchemy.orm import Session
from models import Job, Subscriber
from schemas import JobCreate, SubscribeIn
from sqlalchemy import select

def create_job(db: Session, data: JobCreate) -> Job:
    job = Job(**data.model_dump())
    db.add(job)
    db.commit()
    db.refresh(job)
    return job

def list_jobs(db: Session, limit: int = 50):
    stmt = select(Job).order_by(Job.created_at.desc()).limit(limit)
    return db.execute(stmt).scalars().all()

def add_subscriber(db: Session, data: SubscribeIn) -> Subscriber:
    sub = Subscriber(email=data.email, prefs=data.prefs)
    db.add(sub)
    db.commit()
    db.refresh(sub)
    return sub
