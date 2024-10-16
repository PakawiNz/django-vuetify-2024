FROM node:22-slim as base-vue

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
RUN pip3 install gunicorn uvicorn[standard]

FROM base-vue as built-vue
COPY ./vue/src/ /app/src/
COPY ./vue/public/ /app/public/
COPY ./vue/*config.js /app/
COPY ./vue/jsconfig.json /app/
COPY ./vue/index.html /app/
RUN npm run build

FROM base-python as built-python
COPY ./ /app/
COPY --from=built-vue /app/dist/ /app/vue/dist/

RUN python3 manage.py check
RUN python3 manage.py migrate --plan
RUN python3 manage.py collectstatic --no-input

CMD gunicorn config.asgi --keep-alive 60

EXPOSE 8000
