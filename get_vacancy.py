from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import database_url
from models import Vacancy


engine = create_engine(database_url)
Session = sessionmaker(bind=engine)
session = Session()


vacancies = session.query(Vacancy).filter_by(is_applied=False).all()
with open("vacancies.txt", "w", encoding="utf-8") as f:
    for vacancy in vacancies:
        f.write(f"{vacancy.link}\n")
