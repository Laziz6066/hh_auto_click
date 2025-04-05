import time
from models import Vacancy
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from config import cover_letter_text

def apply_to_vacancies(driver, session, MAX_APPLICATIONS):
    vacancies = session.query(Vacancy).filter_by(is_applied=False).limit(MAX_APPLICATIONS).all()
    print(f"Будет обработано до {MAX_APPLICATIONS} вакансий (доступно: {len(vacancies)})")

    count = 0
    for vacancy in vacancies:
        try:
            print(f"[{count+1}] Открываю: {vacancy.link}")
            driver.get(vacancy.link)
            time.sleep(3)

            button = driver.find_element(By.XPATH,
                                         "//span[contains(@class, 'magritte-button__label') "
                                         "and text()='Откликнуться']")
            button.click()
            print(f"✅ Отклик отправлен: {vacancy.title}")
            time.sleep(2)

            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "textarea.magritte-native-element___a0RAE_2-1-10"))
            )

            # Вводим текст в поле

            textarea = driver.find_element(By.CSS_SELECTOR, "textarea.magritte-native-element___a0RAE_2-1-10")
            textarea.clear()
            textarea.send_keys(cover_letter_text)
            time.sleep(2)
            # Нажимаем кнопку "Отправить"
            submit_button = driver.find_element(By.CSS_SELECTOR, "button[data-qa='vacancy-response-letter-submit']")
            submit_button.click()

            vacancy.is_applied = True
            session.commit()
            count += 1

            if count >= MAX_APPLICATIONS:
                print(f"Достигнуто максимальное количество откликов: {MAX_APPLICATIONS}")
                break

        except Exception as e:
            print(f"⚠️ Ошибка при отклике на {vacancy.link}: {e}")
            continue
    time.sleep(5)
    print("Завершено.")
    driver.quit()