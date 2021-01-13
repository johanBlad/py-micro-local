FROM python:3.8-buster

WORKDIR /app

ADD . /app
COPY start-django.sh /app

RUN pip install -r requirements.txt
#RUN chown -R www-data:www-data /app

EXPOSE 8010

RUN ls -l

CMD ["sh", "start-django.sh"]