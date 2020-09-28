FROM python:3-onbuild

RUN pip3 install  virtualenv --upgrade pip
RUN virtualenv flask
RUN pip install -r requirements.txt
RUN apt-get update && apt-get install -y \ 
curl
EXPOSE 5000

CMD ["python","./app.py"]
