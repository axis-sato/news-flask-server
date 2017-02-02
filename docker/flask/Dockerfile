FROM python:3.6

LABEL maintainer="c8112002"

WORKDIR /app

RUN pip install flask uwsgi

ENTRYPOINT ["uwsgi", "--ini", "uwsgi.ini"]
