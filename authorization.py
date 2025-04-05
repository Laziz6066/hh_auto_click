import time
import json
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import service, user_agent, database_url, MAX_APPLICATIONS
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from responses import apply_to_vacancies


load_dotenv()

COOKIES_FILE = "hh_cookies.json"
LOGIN_URL = "https://hh.ru/account/login"
BASE_URL = "https://hh.ru/"

options = webdriver.ChromeOptions()
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument(user_agent)

driver = webdriver.Chrome(service=service, options=options)

engine = create_engine(database_url)
Session = sessionmaker(bind=engine)
session = Session()


def save_cookies():
    """Сохраняет cookies в файл после ручной авторизации."""
    input("1. Войдите вручную в открывшемся браузере и нажмите Enter в этом окне терминала...")
    cookies = driver.get_cookies()
    with open(COOKIES_FILE, 'w') as f:
        json.dump(cookies, f)
    print("✅ Cookies сохранены в файл!")


def load_cookies():
    """Загружает cookies из файла и проверяет их валидность."""
    if not os.path.exists(COOKIES_FILE):
        return False

    driver.get(BASE_URL)
    time.sleep(2)

    with open(COOKIES_FILE, 'r') as f:
        cookies = json.load(f)

    for cookie in cookies:
        cookie.pop('sameSite', None)
        driver.add_cookie(cookie)

    print("🔹 Cookies загружены. Проверяем авторизацию...")
    driver.refresh()
    time.sleep(3)

    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[data-qa="mainmenu_myResumes"]')))
        print("✅ Авторизация через cookies успешна!")
        return True
    except:
        print("❌ Cookies недействительны. Требуется новая авторизация.")
        os.remove(COOKIES_FILE)
        return False


def auth_with_cookies():
    """Основная логика авторизации через cookies или ручной вход."""
    if load_cookies():
        return True

    print("🔹 Открываю страницу для ручного входа...")
    driver.get(LOGIN_URL)
    save_cookies()
    return True


def main():
    if not auth_with_cookies():
        print("Не удалось авторизоваться. Закрываю браузер.")
        driver.quit()
        return

    print("Готово! Скрипт может продолжать работу с вашим аккаунтом.")
    apply_to_vacancies(driver, session, MAX_APPLICATIONS)
    time.sleep(10)
    driver.quit()


if __name__ == "__main__":
    main()