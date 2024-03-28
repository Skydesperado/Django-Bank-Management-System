FROM python:3.11-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

COPY requirements.txt /app/

RUN pip install --upgrade pip && pip install -r requirements.txt

RUN apt-get update && apt-get install -y curl

COPY . /app/

RUN python /app/backend/manage.py collectstatic --noinput

EXPOSE 8000

CMD ["gunicorn", "backend.config.wsgi:application", "--bind", "0.0.0.0:8000"]

HEALTHCHECK --interval=20s --timeout=10s CMD curl -f http://localhost:8000/ || exit 1
