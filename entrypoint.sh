#!/bin/bash

# Функция для ожидания доступности порта
# wait_for_port() {
#     local host="$1"
#     local port="$2"
#     local timeout=10
#     local start_time=$(date +%s)

#     # Попробовать использовать nc, если установлен
#     local nc_command="nc"
#     type $nc_command >/dev/null 2>&1 || nc_command="ncat"

#     while ! $nc_command -z "$host" "$port" >/dev/null 2>&1; do
#         sleep 1
#         local current_time=$(date +%s)
#         local elapsed_time=$((current_time - start_time))
#         echo "trying to connecto to pg via $host:$port"

#         if [ $elapsed_time -ge $timeout ]; then
#             echo "Unable to connect to pg"
#             exit 1
#         fi
#     done
# }

# # Ожидание доступности порта PostgreSQL
# wait_for_port "postgres" 5432

# Запуск Django-приложения
# python manage.py runserver 0.0.0.0:8000

# python manage.py collectstatic --noinput
python manage.py makemigrations
python manage.py migrate
gunicorn core.project.wsgi:application --bind 0.0.0.0:8000 --workers 3 --threads 2 --timeout 30
gunicorn --log-file=- core.project.wsgi:application
