from models import Vacancy
from config import database_url
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine(database_url)
Session = sessionmaker(bind=engine)
session = Session()

user_link = input("Отправьте ссылку вакансии: ").strip()

vacancy = session.query(Vacancy).filter_by(link=user_link, is_applied=False).first()

if vacancy:
    vacancy.is_applied = True
    session.commit()
    print("✅ Статус вакансии обновлён: is_applied = True")
else:
    print("❌ Вакансия не найдена или уже отмечена как откликнутая.")
