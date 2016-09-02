# from __future__ import absolute_import
from celery import Celery


# app = Celery('tasks',
#              broker='redis://localhost:6379',
#              backend='redis://',
#              include=['task_queue_celery.tasks'])

app = Celery('tasks',
             broker='redis://localhost:6379',
             backend='redis://'
             )

app.conf.update(
    CELERY_TASK_RESULT_EXPIRES=3600,
)


if __name__ == '__main__':
    app.start()