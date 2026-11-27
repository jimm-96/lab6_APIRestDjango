#!/usr/bin/env bash
# Script de build para Render.
set -o errexit

pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate

# Crea el usuario del admin si se definieron las variables DJANGO_SUPERUSER_*.
if [[ -n "${DJANGO_SUPERUSER_USERNAME:-}" ]]; then
    python manage.py createsuperuser --no-input || echo "El superusuario no se creó (puede que ya exista)."
fi
