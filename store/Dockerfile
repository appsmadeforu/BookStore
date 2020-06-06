# pull official base image
FROM python:3.8.0-alpine

# set work directory
WORKDIR /www/store

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY requirements.txt /www/store/requirements.txt
#RUN apk add --no-cache python3-dev openssl-dev libffi-dev gcc
RUN apk add python python-dev py-pip postgresql-dev musl-dev build-base libffi-dev openssl-dev libgcc && apk add jpeg-dev zlib-dev libjpeg \
    && pip install Pillow

RUN pip --no-cache-dir install -r requirements.txt

ARG DEBUG=True
RUN if [[ $DEBUG = 'False' ]]; then make collectstatic; fi


# copy entrypoint.sh
COPY ./entrypoint.sh /www/store/entrypoint.sh

# copy project
COPY . /www/store/

# run entrypoint.sh
ENTRYPOINT ["/www/store/entrypoint.sh"]