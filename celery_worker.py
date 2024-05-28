from app import create_app
from app.tasks import celery, init_celery

app = create_app()
init_celery(app)

if __name__ == '__main__':
    celery.start()
