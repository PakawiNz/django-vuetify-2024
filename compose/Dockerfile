FROM node:22-slim as base-nodejs

WORKDIR /app/

COPY ./vue/package.json /app/
RUN npm install

FROM python:3.12-slim as base-python

# [required for runserver in docker]
# to ensures the python output i.e. the stdout and stderr streams are sent straight to terminal (e.g. your container log)
# without being first buffered and that you can see the output of your application (e.g. django logs) in real time.
ENV PYTHONUNBUFFERED 1

WORKDIR /app/

COPY ./requirements.txt /requirements.txt
RUN pip3 install -r /requirements.txt
