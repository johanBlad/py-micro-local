FROM python:3.8-buster

WORKDIR /app

ADD . /app

RUN pip install -r requirements.txt

EXPOSE 8001

CMD ["gunicorn", "-w", "3", "--bind", "0.0.0.0:8001", "wsgi:application"]