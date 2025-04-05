import os
from selenium.webdriver.chrome.service import Service
from dotenv import load_dotenv


load_dotenv()

driver_path = os.getenv("DRIVER_PATH")
user_agent = os.getenv("USER_AGENT")
database_url = os.getenv("DATABASE_URL")


MAX_APPLICATIONS = 200

service = Service(executable_path=driver_path)

cover_letter_text = ("Здравствуйте!\nМеня заинтересовала ваша вакансия Python-разработчика.\n"
                     "Я Python-разработчик с более чем 3 годами опыта в backend-разработке. "
                     "Мой стек:  Django, FastAPI, PostgreSQL, SQLAlchemy, Celery, Redis, Docker, "
                     "CI/CD, Git, Pytest, Linux. Имею опыт работы с высоконагруженными API, "
                     "оптимизации запросов в PostgreSQL и интеграции с внешними сервисами.\n"
                     "Меня привлекает возможность работать над интересными задачами. Уверен, что "
                     "мой опыт позволит внести ценный вклад в развитие вашей компании.\n"
                     "Буду рад обсудить детали сотрудничества!\nКонтакты:\nEmail: "
                     "lazizpython@gmail.com\nTelegram: @laziz_python\nС уважением,\nЛазиз")