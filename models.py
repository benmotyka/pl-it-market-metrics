from os import environ
from datetime import datetime
from uuid import uuid4
from dotenv import load_dotenv
from sqlalchemy import create_engine, Column, String, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.dialects.postgresql import UUID

load_dotenv()

engine = create_engine(environ.get("DATABASE_URL"), echo=True)
Base = declarative_base()


class ActivityModel(Base):
    __tablename__ = 'activity'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    created_at = Column(DateTime, default=datetime.utcnow)
    domain = Column(String(30), nullable=False)

Session = sessionmaker(bind=engine)

session = Session()
