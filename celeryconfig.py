__author__ = 'dean.hutton'
BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
#CELERY_TASK_RESULT_EXPIRES = 18000  # 5 hours. default is 24 hours