FROM python:3.6

LABEL maintainer="c8112002"

WORKDIR /app

RUN pip install flask uwsgi

EXPOSE 80

ENTRYPOINT ["uwsgi", "--socket", "0.0.0.0:80", "--protocol=http", "-w", "wsgi:app"]