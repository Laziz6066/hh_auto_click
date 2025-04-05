import time
from bs4 import BeautifulSoup
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from selenium import webdriver
from config import service, user_agent, database_url
from dotenv import load_dotenv
from models import Base, Vacancy

load_dotenv()


options = webdriver.ChromeOptions()
options.add_argument(user_agent)
driver = webdriver.Chrome(service=service, options=options)

engine = create_engine(database_url)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

def jobs(job_url):
    driver.get(job_url)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    driver.execute_script("window.scrollTo({top: document.body.scrollHeight, behavior: 'smooth'});")
    for _ in range(5):
        driver.execute_script("window.scrollBy(0, 500);")
        time.sleep(1)

    html = driver.page_source
    soup = BeautifulSoup(html, "lxml")
    vacancies = soup.find_all('div', class_='magritte-redesign')

    print(f"Найдено вакансий: {len(vacancies)}")

    for vacancy in vacancies:
        title = vacancy.find('a', {'data-qa': 'serp-item__title'})
        title_text = title.text.strip() if title else "Название не указано"
        link = title['href'] if title else "Ссылка не указана"

        if session.query(Vacancy).filter_by(link=link).first():
            print(f"Дубликат: {link}")
            continue

        company = vacancy.find('a', {'data-qa': 'vacancy-serp__vacancy-employer'})
        company_text = company.text.strip() if company else "Компания не указана"

        new_vacancy = Vacancy(
            title=title_text,
            link=link,
            company=company_text,
            is_applied=False
        )

        session.add(new_vacancy)
        session.commit()

        print(f"Добавлено: {title_text} — {company_text}")

def main():
    for i in range(2):
        print(f"Страница {i}", '-' * 50)
        url = (f"https://hh.ru/search/vacancy?text=python&salary=&ored_clusters=true&page={i}"
               f"&searchSessionId=955a671a-bb40-4945-9489-9550f2b67771")
        jobs(url)
        time.sleep(3)
    print("Парсинг завершён. Данные сохранены в БД.")

if __name__ == "__main__":
    main()