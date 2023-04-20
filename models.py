from os import environ
from dotenv import load_dotenv
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker

load_dotenv()

engine = create_engine(environ.get("DATABASE_URL"), echo=True)
Base = declarative_base()

class ActivityModel(Base):
    __tablename__ = 'activity'

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime)
    domain = Column(String(30), nullable=False) 

Session = sessionmaker(bind=engine)

session = Session()