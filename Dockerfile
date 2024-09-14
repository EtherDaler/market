FROM python:3.11-alpine

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
COPY ./entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Install postgres client
RUN apk add --update --no-cache postgresql-client \
    gcc libc-dev linux-headers postgresql-dev \
        && apk add libffi-dev

# Install individual dependencies
# so that we could avoid installing extra packages to the container
RUN apk add --update --no-cache --virtual .tmp-build-deps \
	gcc libc-dev linux-headers postgresql-dev
RUN pip install -r /requirements.txt

# Remove dependencies
RUN apk del .tmp-build-deps

RUN mkdir /app
WORKDIR /app
COPY . .
EXPOSE 8000
# [Security] Limit the scope of user who run the docker image
# RUN adduser -D user

# USER user
