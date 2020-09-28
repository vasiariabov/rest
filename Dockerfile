FROM python:2.7.18-alpine3.11

COPY requirements.txt /

RUN pip install -r /requirements.txt

COPY src/ /app

WORKDIR /app

EXPOSE 8000

CMD ["gunicorn", "-w 4", "-b :8000", "app:app"]