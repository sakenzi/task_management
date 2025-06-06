## Установка и запуск

1. Создайте папку для проекта
2. Склонируйте репозиторий:

   ```bash
   git clone https://github.com/sakenzi/task_management.git
   ```
3. Установите `virtualenv`:

   ```bash
   pip install virtualenv
   ```
4. Создайте виртуальное окружение:

   ```bash
   python -m venv env
   ```
5. Активируйте окружение:

   ```bash
   env\Scripts\activate
   ```
6. Установите зависимости:

   ```bash
   pip install -r requirements.txt
   ```
7. Создайте базу данных в PostgreSQL с параметрами, указанными в .env (пример команды):

   ```bash
   CREATE DATABASE task_db;
   ```
8. Примените миграции Alembic:

   ```bash
   alembic upgrade head
   ```
9. Создайте файл `.env` в корне проекта и добавьте в него переменные:

   ```env
   DB_HOST=localhost
   DB_PORT=5432
   DB_USER=your_user
   DB_PASS=your_password
   DB_NAME=task_db
   TOKEN_SECRET_KEY=your_secret_key
   ```
10. Запустите проект:

   ```bash
   python run.py
   ```
11. Откройте Swagger:
   [http://localhost:8000/docs](http://localhost:8000/docs)
12. Готово — тестируйте API!
