from os import environ
from datetime import datetime
from uuid import uuid4
from dotenv import load_dotenv
from sqlalchemy import create_engine, Column, String, DateTime, Integer
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


class PositionsModel(Base):
    __tablename__ = 'positions'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    domain = Column(String(30), nullable=False)
    overall = Column(Integer, nullable=False)
    remote_count = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)


class SeniorityModel(Base):
    __tablename__ = 'seniority'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    domain = Column(String(30), nullable=False)
    seniority = Column(String(20), nullable=False)
    count = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)


class LocalizationModel(Base):
    __tablename__ = 'localization'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    domain = Column(String(30), nullable=False)
    city = Column(String(50), nullable=False)
    count = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)


Session = sessionmaker(bind=engine)

session = Session()
