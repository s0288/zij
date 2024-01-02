FROM python:3.11-alpine

WORKDIR '/app'

# install dependencies
COPY requirements.txt .
# need to run requirements.txt like this
# because of argon2
RUN apk add gcc musl-dev libffi-dev && \
    pip install -U  cffi pip setuptools && \
    pip3 install --no-cache-dir -r requirements.txt

# set time zone
ENV TZ=Europe/Berlin
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# mount relevant directories
COPY ./src .

EXPOSE 8000

# default command to execute
CMD exec gunicorn zij.wsgi:application --bind 0.0.0.0:8000 --workers 3
