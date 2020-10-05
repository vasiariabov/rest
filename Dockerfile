FROM python:3.6-alpine3.11

COPY requirements.txt /

RUN pip install -r /requirements.txt
RUN python setup.py build_ext --pg-config /path/to/pg_config build ...
RUN pip install psycopg2-binary
COPY src/ /app

WORKDIR /app

EXPOSE 8000

CMD ["gunicorn", "-w 4", "-b :8000", "app:app"]
