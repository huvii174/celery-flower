from celery import Celery

celery = Celery()

def init_celery(app):
    celery.conf.update(
        broker_url=app.config['CELERY_BROKER_URL'],
        result_backend=app.config['CELERY_RESULT_BACKEND']
    )
    celery.autodiscover_tasks(['app.tasks'])

@celery.task
def add_together(a, b):
    return a + b
