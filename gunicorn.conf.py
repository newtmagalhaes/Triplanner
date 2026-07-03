import os
import multiprocessing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'triplanner.settings')

wsgi_app = 'triplanner.wsgi'

workers = min(multiprocessing.cpu_count(), 2)
max_requests = 100
max_requests_jitter = 50

# Logging
loglevel = os.getenv("GUNICORN_LOG_LEVEL", "info")
