FROM python:3.6-alpine3.11
RUN apk update && apk add bash && apk add postgresql-dev gcc python3-dev musl-dev 

COPY requirements.txt /

RUN pip3 install -r /requirements.txt --no-cache-dir

COPY . /app

WORKDIR /app/src

EXPOSE 8000

CMD ["gunicorn", "-w 4", "-b :8000", "app:app"]
