from sqlalchemy import Column,Integer, String,DateTime,create_engine
from sqlalchemy.orm import DeclarativeBase,Mapped,mapped_column,Session
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

engine = create_engine(os.getenv("DATABASE","sqlite:///database.db"),echo=True)

class Base(DeclarativeBase):
    pass

class Challenge(Base):
    __tablename__ = "challenges"
    id:Mapped[int] = mapped_column(Integer,primary_key=True)
    difficulty:Mapped[str] = mapped_column(String,nullable=False)
    date_created:Mapped[datetime] = mapped_column(DateTime,default=datetime.now)
    created_by:Mapped[str] = mapped_column(String,nullable=False)
    title:Mapped[str] = mapped_column(String,nullable=False)
    options:Mapped[str] = mapped_column(String,nullable=False)
    correct_answer_id:Mapped[int] = mapped_column(Integer,nullable=False)
    explanation:Mapped[str] = mapped_column(String,nullable=False)

class ChallengeQuota(Base):
    __tablename__ = "challenge_quotas"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id:Mapped[str] = mapped_column(String,nullable=False,unique=True)
    quota_remaining:Mapped[int] = mapped_column(Integer,nullable=False,default=50)
    last_reset_date:Mapped[datetime] = mapped_column(DateTime,default=datetime.now)

Base.metadata.create_all(bind=engine)

def get_session():
    with Session(engine) as session:
        yield session