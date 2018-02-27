FROM python:3.5.2-alpine


RUN apk update && apk add \
    build-base \
    jpeg-dev \
    zlib-dev \
    libpq \
    postgresql-dev \
    gettext

WORKDIR /hotels

COPY requirements.txt hotels/requirements.txt
RUN pip install -r hotels/requirements.txt

COPY docker-entrypoint-api.sh /docker-entrypoint-api.sh
RUN chmod +x /docker-entrypoint-api.sh


COPY . /hotels

EXPOSE 8000

ENTRYPOINT /docker-entrypoint-api.sh
