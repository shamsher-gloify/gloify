from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gloify.settings')

celery = Celery('gloify')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
celery.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
celery.autodiscover_tasks()

# Add this line to address the deprecation warning 
broker_connection_retry_on_startup = True 
@celery.task(bind=True) 
def debug_task(self):     
    print(f'request: {self.request!r}')



# Configure Celery Beat

# celery.conf.beat_schedule = {
#     'task-name': {
#         'task': 'myapp.tasks.my_task',  # Path to your task
#         'schedule': crontab(minute='*/15'),  # Run every 15 minutes
#     },
# }

celery.conf.beat_schedule = {
    'beat_test': {
        'task': 'beat_test',  # name of your task
        'schedule': crontab(minute='*/1'),  # Run every 1 minutes
        # 'schedule': 5.0, # Run every 5 seconds
    },
}