from flask import Flask
from celery import Celery
from pallets.core.configs import configs
from pallets.core.blueprints import blueprints
from pallets.core.extensions import extensions


CELERY_TASK_LIST = ['pallets.blueprints.contact.tasks']


def create_app(settings_override=None):
    """
        Create application by using factory pattern.
        :return: Flask app
    """
    app = Flask(__name__, instance_relative_config=True)

    # Config
    configs(app, settings_override)

    # Blueprints
    blueprints(app)

    # Extensions
    extensions(app)

    return app


def create_celery_app(app=None):
    """
        Create a new Celery object via Celery config to the app's config.
        Wrap all tasks in the context of the application.

        :param app: Flask app
        :return: Celery app
    """
    app = app or create_app()

    celery = Celery(
        app.import_name,
        broker=app.config['CELERY_BROKER_URL'],
        include=CELERY_TASK_LIST,
    )

    celery.conf.update(app.config)
    TaskBase = celery.Task

    class ContextTask(TaskBase): # noqa
        abstract = True

        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)

    celery.Task = ContextTask
    return celery
