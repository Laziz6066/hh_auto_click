import os
from selenium.webdriver.chrome.service import Service
from dotenv import load_dotenv


load_dotenv()

driver_path = os.getenv("DRIVER_PATH")
user_agent = os.getenv("USER_AGENT")
database_url = os.getenv("DATABASE_URL")


MAX_APPLICATIONS = 200

service = Service(executable_path=driver_path)

cover_letter_text = ("Тут будет ваше сопроводительное письмо")