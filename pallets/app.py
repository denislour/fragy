from flask import Flask
from pallets.blueprints.page import page
from pallets.extensions import debug_toolbar


def create_app(settings_override=None):
    """
        Create application by using factory pattern.
        :return: Flask app
    """
    app = Flask(__name__, instance_relative_config=True)

    # Config
    config(app, settings_override)

    # Blueprints
    blueprint(app)

    # Extensions
    extensions(app)

    return app


def extensions(app):
    """
        Register the extensions (mutates the app passing in).

        :params: Flask app instance
        :return: None
    """
    debug_toolbar.init_app(app)


def blueprint(app):
    """
        Register the blueprint (mutates the app passing in).

        :params: Flask app instance
        :return: None
    """
    app.register_blueprint(page)

def config(app, settings_override):
    """
        Config app (mutates the app passing in).

        :params: Flask app instance
        :return: None
    """
    app.config.from_object("config.settings")
    app.config.from_pyfile("settings.py", silent=True)

    if settings_override is not None:
        app.config.update(settings_override)
