import os
import logging.config


class DevConfig:
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    AWS_BUCKET_NAME = os.environ.get('S3_BUCKET_NAME')
    AWS_REGION = os.environ.get('S3_REGION')
    AWS_ACL = 'public-read'
    LOG_FORMAT = '%(asctime)s %(name)s:%(lineno)d [%(levelname)-4s] %(message)s'
    TASK_RESULT_EXPIRED_SEC = None
    logging.config.dictConfig({
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'standard': {
                'format': LOG_FORMAT,
                'datefmt': '%Y-%m-%d %H:%M:%S'
            },
        },
        'handlers': {
            'console': {
                'level': 'DEBUG',
                'class': 'logging.StreamHandler',
                'formatter': 'standard'
            },
        },
        'loggers': {
            '': {
                'handlers': ['console'],
                'level': 'DEBUG',
                'propagate': True
            },
        }
    })
