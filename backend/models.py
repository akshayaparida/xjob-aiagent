from sqlalchemy import Column, Integer, String, Text, TIMESTAMP, func, Index
from db import Base

class Job(Base):
    __tablename__ = "jobs"
    id = Column(Integer, primary_key=True)
    tweet_id = Column(String(50), unique=True, nullable=True)
    title = Column(String(255))
    company = Column(String(255))
    location = Column(String(255))
    url = Column(Text)
    raw_text = Column(Text, nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.now())

Index("ix_jobs_created_at", Job.created_at.desc())

class Subscriber(Base):
    __tablename__ = "subscribers"
    id = Column(Integer, primary_key=True)
    email = Column(String(255), unique=True, nullable=False)
    prefs = Column(Text, nullable=True)  # JSON string later if you want
    subscribed_at = Column(TIMESTAMP, server_default=func.now())
