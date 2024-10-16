from settings import *
import os
import dj_database_url 

DATABASES = {
    'default': dj_database_url.config(
        env='DATABASE_URL',
        conn_max_age=600,
        ssl_require=True,
        conn_health_checks=True
        )
}

CELERY_BROKER_URL = config('REDIS_URL', 'redis://redis:6379/0')

CELERY_RESULT_BACKEND = CELERY_BROKER_URL
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_SERIALIZER = 'json'

CACHE = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': config('REDIS_URL'),
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
}

DEBUG = False

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': ('%(asctime)s [%(process)d] [%(levelname)s] ' + 
                        'pathname=%(pathname)s lineno=%(lineno)d' +
                        'funcname=%(funcName)s  %(message)s'),
            'datefmt': '%Y-%m-%d %H:%M:%S',            
        },
        'simple': {
            'format': '{levelname} {message}',
        },
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'testlogger': {
            'handlers': ['console'],
            'level': 'INFO',
        }
    },    
    'root': {
        'handlers': ['console'],
        'level': 'DEBUG',
    },    
    'django.db.backends': {
        'handlers': ['console'],
        'level': 'DEBUG',
    },
    'django.request': {
        'handlers': ['console'],
        'level': 'DEBUG',
        'propagate': False,
    },
    'django.security.csrf': {
        'handlers': ['console'],
        'level': 'DEBUG',
        'propagate': False,
    }
}