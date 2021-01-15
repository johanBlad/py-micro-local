FROM python:3.8-buster

WORKDIR /app

ADD . /app
COPY start-django.sh /app

RUN pip install -r requirements.txt

EXPOSE 8002

CMD ["sh", "start-django.sh"]