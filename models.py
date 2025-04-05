from sqlalchemy import Column, String, Boolean, Integer
from sqlalchemy.orm import declarative_base


Base = declarative_base()


class Vacancy(Base):
    __tablename__ = 'vacancies'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    link = Column(String, unique=True, index=True)
    company = Column(String)
    is_applied = Column(Boolean, default=False)
