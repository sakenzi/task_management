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
7. Создайте файл `.env` в корне проекта и добавьте в него переменные:

   ```env
   DB_HOST=...
   DB_PORT=...
   DB_NAME=...
   DB_USER=...
   DB_PASS=...
   TOKEN_SECRET_KEY=...
   ```
8. Запустите проект:

   ```bash
   python run.py
   ```
9. Откройте Swagger:
   [http://localhost:8000/docs](http://localhost:8000/docs)
10. Готово — тестируйте API!
