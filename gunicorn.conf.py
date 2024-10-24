# https://docs.gunicorn.org/en/latest/settings.html#settings
import multiprocessing

bind = '0.0.0.0:8000'
worker_class = 'uvicorn.workers.UvicornWorker'
workers = multiprocessing.cpu_count() * 2 + 1
timeout = 300

accesslog = '-'
errorlog = '-'
