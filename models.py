from datetime import datetime   

from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class ActivityModel(Base):
    __tablename__ = 'activity'

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime)
    domain = Column(String(30), nullable=False) 
