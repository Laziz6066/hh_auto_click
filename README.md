# Авто отклик на hh.ru
#### (проект разработан исключительно в учебных и ознакомительных целях)
## Описание проекта

### Проект предназначен для автоматических откликов на вакансии сайта hh.ru. С его помощью пользователи могут:
#### * Парсить вакансии с hh.ru
#### * Авторизоваться под своей учетной записью для авто откликов

## Установка и запуск
### 1. Клонирование репозитория
#### Клонируйте репозиторий с помощью команды:
```aiignore
https://github.com/Laziz6066/hh_auto_click.git
```
### 2. Создание и активация виртуального окружения
#### Для Windows:
```aiignore
python -m venv venv
venv\Scripts\activate

```
### 3. Установка зависимостей
```aiignore
pip install -r requirements.txt
 
```
### 4. Укажите свои данные
#### В файле ```.env.template``` укажите свой user_agent (user_agent можно получить перейдя по этой [ссылке](https://n5m.ru/usagent.html));
#### Напишите свой URL для подключения к PostgreSQL в поле: DATABASE_URL;
#### Для DRIVER_PATH укажите полный путь к ```chromedriver.exe``` (скачать можно по этой [ссылке](https://github.com/jsnjack/chromedriver/releases)).

### 5. Для парсинга вакансий 
#### Перейдите в [job_parsing.py](job_parsing.py) и запустите 
```shell
  if __name__ == "__main__":
      main()
```
#### по умолчанию скрипт парсит первые 2 страницы python вакансий но вы можете изменить число страниц и url в функции main()
### 6. Для авто откликов из учетной записи
#### Перейдите в файл [authorization.py](authorization.py) и запустите 
```shell
  if __name__ == "__main__":
      main()
```
#### откроется окно авторизации после того как вы авторизовались перейдите в терминал и нажмите на кнопку ```Enter```

### 7. Ручной отклик
#### Из-за того что скрипт (пока что) написан не целиком могут возникнуть некоторые сложности с авто откликами и на некоторые вакансии нам придется в ручную откликнуться. Для этого переходим в файл [get_vacancy.py](get_vacancy.py) и запускаем после этого у нас появиться файл ```vacancies.txt``` внутри него находятся те ссылки на которые бот не смог откликнуться. После того как мы откликнулись на эти вакансии в ручную переходим в файл [change_status.py](change_status.py) и запускаем, после отправляем ссылку а бот изменит статус ссылки в бд.
