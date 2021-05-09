FROM python:3.9.5-alpine

RUN apk update && apk upgrade && \
    apk add \
    git

RUN mkdir /code && \
    cd /code && \
    git clone https://github.com/AdamOsiowy/django_server.git . && \
    pip3 install -r requirements.txt

RUN apk del \
    git

COPY . /code

EXPOSE 8000

WORKDIR /code

CMD python3.9 django_server/manage.py runserver 0.0.0.0:8000
