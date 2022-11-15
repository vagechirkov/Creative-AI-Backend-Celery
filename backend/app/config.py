import os

REDIS_HOST = os.environ.get('REDIS_HOST')
REDIS_PORT = os.environ.get('REDIS_PORT')
REDIS_CELERY_DB_INDEX = os.environ.get('REDIS_CELERY_DB_INDEX')

# redis://:password@hostname:port/db_number
BROKER_CONN_URI = f"redis://{REDIS_HOST}:{REDIS_PORT}/{REDIS_CELERY_DB_INDEX}"
BACKEND_CONN_URI = f"redis://{REDIS_HOST}:{REDIS_PORT}/{REDIS_CELERY_DB_INDEX}"

TASK_QUEUE = os.environ.get('TASK_QUEUE', 'generate_image')

# S3
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
S3_ROLE_ARN = os.environ.get('S3_ROLE_ARN')
BUCKET_NAME = os.environ.get('BUCKET_NAME', 'creativeai-20221111143400')

# Logs
LOGZIO_URL = os.environ.get('LOGZIO_URL')
LOGZIO_TOKEN = os.environ.get('LOGZIO_TOKEN')
