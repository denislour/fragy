from flask import Flask
from pallets.blueprints.page import page


def create_app(settings_override=None):
    """
        Create application by using factory pattern.
        :return: Flask app
    """
    app = Flask(__name__, instance_relative_config=True)

    # Config
    app.config.from_object("config.settings")
    app.config.from_pyfile("settings.py", silent=True)

    if settings_override is not None:
        app.config.update(settings_override)

    # Blueprints
    app.register_blueprint(page)

    return app
