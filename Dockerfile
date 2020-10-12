FROM python:3.6-alpine3.11
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev 
RUN pip install psycopg2-binary

COPY requirements.txt /

RUN pip install -r /requirements.txt


COPY src/ /app

WORKDIR /app

EXPOSE 8000

CMD ["gunicorn", "-w 4", "-b :8000", "app:app"]
