#!/bin/bash

# Сборка статических файлов
python manage.py collectstatic --noinput

# Миграция базы данных
python manage.py migrate

# Создание админки
python manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.filter(username='root').exists() or User.objects.create_superuser('admin', 'admin@example.com', 'admin')"

# Запуск сервера
exec gunicorn Home_aid_kit_API.wsgi:application --bind 0.0.0.0:8000