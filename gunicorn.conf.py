# https://docs.gunicorn.org/en/latest/settings.html#settings
import multiprocessing

bind = '0.0.0.0:8000'
# worker_class = 'compose.uvicorn_worker.MyUvicornWorker'
workers = multiprocessing.cpu_count() * 2 + 1
timeout = 300

accesslog = '-'
errorlog = '-'
