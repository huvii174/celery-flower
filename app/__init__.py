from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config.update(
        CELERY_BROKER_URL='redis://redis:6379/0',
        CELERY_RESULT_BACKEND='redis://redis:6379/0'
    )

    from .views import main
    app.register_blueprint(main)

    return app
