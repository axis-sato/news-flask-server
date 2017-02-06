FROM python:3.6

LABEL maintainer="c8112002"

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

ENTRYPOINT ["uwsgi", "--ini", "uwsgi.ini"]
