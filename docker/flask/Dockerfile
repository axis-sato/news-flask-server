FROM python:3.6

LABEL maintainer="c8112002"

WORKDIR /app

RUN pip install flask uwsgi

COPY ./docker-entrypoint.sh /
RUN chmod +x /docker-entrypoint.sh
ENTRYPOINT ["/docker-entrypoint.sh"]
