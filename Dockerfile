FROM python:3.7-alpine

RUN mkdir /app
WORKDIR /app
ADD gunicorn.sh /app
ADD cloud_interface.crt /app
ADD cloud_interface.key /app
ADD requirements.txt /app
ADD src/rest.py /app
ADD src/database.db /app

RUN pip3 install -r requirements.txt

ENTRYPOINT ["./gunicorn.sh"]